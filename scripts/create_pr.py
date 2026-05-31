import json
import os
import sys
from datetime import datetime
from github import Github, GithubException

# ---------- Config ----------
# Prefer an explicit PAT if provided (useful when org policies block Actions).
# Workflow can set `PAT_TOKEN` secret; otherwise fall back to the injected `GITHUB_TOKEN`.
TOKEN = os.getenv("PAT_TOKEN") or os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")          # auto-set by GitHub Actions
BASE_BRANCH = os.getenv("BASE_BRANCH", "main")
TARGET_FILE = os.getenv("TARGET_FILE", "app/main.py")
AGENT_RESPONSE = "reports/agent_response.json"
DECISION_FILE = "reports/decision.json"


def print_and_exit(msg: str, code: int = 1):
    print(msg)
    sys.exit(code)


def print_pr_guidance(error_msg: str):
    print(f"❌ PR creation failed: {error_msg}")
    if 'GitHub Actions is not permitted to create or approve pull requests' in error_msg or 'is not permitted to create or approve pull requests' in error_msg:
        print('\nPossible resolutions:')
        print('- Give the workflow `pull-requests: write` and `contents: write` permissions in your workflow YAML:')
        print('  permissions:')
        print('    contents: write')
        print('    pull-requests: write')
        print('\n- Or create a Personal Access Token (classic) or fine-grained token with `repo` scope,')
        print("  store it as a repository secret (e.g. 'PAT_TOKEN') and set the Actions step to use it:")
        print('  env:')
        print('    PAT_TOKEN: ${{ secrets.PAT_TOKEN }}')
        print('\n- If this repo is in an organization, ensure the organization allows workflows to create PRs (organization settings).')


def load_json_or_exit(path: str):
    if not os.path.exists(path):
        print_and_exit(f"❌ {path} not found")
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        print_and_exit(f"❌ Could not read {path}: {e}")


def get_token_source():
    return 'PAT_TOKEN' if os.getenv('PAT_TOKEN') else 'GITHUB_TOKEN'


def get_github_client(token: str):
    try:
        from github import Auth
        return Github(auth=Auth.Token(token))
    except Exception:
        return Github(token)


def create_branch(repo, base_branch: str, branch_name: str):
    base = repo.get_branch(base_branch)
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base.commit.sha)


def update_file_in_branch(repo, target_file: str, fixed_code: str, base_branch: str, branch_name: str):
    contents = repo.get_contents(target_file, ref=base_branch)
    repo.update_file(
        path=target_file,
        message=f"fix(security): AI remediation",
        content=fixed_code,
        sha=contents.sha,
        branch=branch_name
    )


def create_pr_and_labels(repo, title: str, body: str, head: str, base: str, labels: list):
    pr = repo.create_pull(title=title, body=body, head=head, base=base)
    if labels:
        try:
            pr.add_to_labels(*labels)
        except GithubException:
            print("⚠️  Could not add labels (labels may not exist in repo)")
    return pr


def main():
    if not TOKEN or not REPO_NAME:
        print_and_exit("❌ GITHUB token (PAT_TOKEN or GITHUB_TOKEN) or GITHUB_REPOSITORY not set\nIf GitHub Actions cannot create PRs with the default token, add a PAT as a repository secret named 'PAT_TOKEN'")

    print(f"Using token from: {get_token_source()}")

    agent = load_json_or_exit(AGENT_RESPONSE)
    decision = load_json_or_exit(DECISION_FILE)

    severity = agent.get("severity", "UNKNOWN")
    confidence = agent.get("confidence_score", 0)
    summary = agent.get("summary", "AI-generated security remediation")
    fixed_code = agent.get("fixed_code", "").strip()
    recommendations = agent.get("recommendations", [])
    auto_fix = decision.get("auto_fix", False)

    if not fixed_code:
        print_and_exit("⚠️  No fixed_code from AI agent — skipping PR", 0)

    g = get_github_client(TOKEN)
    repo = g.get_repo(REPO_NAME)

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    branch_name = f"ai-remediation/{severity.lower()}-{timestamp}"

    try:
        create_branch(repo, BASE_BRANCH, branch_name)
        print(f"✅ Branch created: {branch_name}")
    except GithubException as e:
        print_and_exit(f"❌ Branch creation failed: {e}")

    try:
        update_file_in_branch(repo, TARGET_FILE, fixed_code, BASE_BRANCH, branch_name)
        print(f"✅ {TARGET_FILE} updated on {branch_name}")
    except GithubException as e:
        print_and_exit(f"❌ File update failed: {e}")

    recs = "\n".join(f"- {r}" for r in recommendations) or "_None provided_"
    auto_merge_note = (
        "🟢 **Auto-merge eligible** — will merge after CI passes." if auto_fix else "🚨 **Human approval required** — please review before merging."
    )

    body = f"""## 🤖 AI Security Remediation

{auto_merge_note}

### 📊 Analysis
- **Severity:** `{severity}`
- **Confidence:** `{confidence}%`
- **Auto-fix allowed:** `{auto_fix}`

### 📝 Summary
{summary}

### 🛡️ Recommendations
{recs}

### 🔧 Changed Files
- `{TARGET_FILE}`

---
_Generated by **Agentic Self-Healing CI/CD Pipeline** • {datetime.utcnow().isoformat()}Z_
"""

    title = f"[AI-Remediation] {severity} severity fix in {TARGET_FILE}"
    labels = ["ai-remediation", f"severity-{severity.lower()}"]
    if not auto_fix:
        labels.append("needs-human-review")

    try:
        pr = create_pr_and_labels(repo, title, body, branch_name, BASE_BRANCH, labels)
        print(f"✅ PR created: {pr.html_url}")
    except GithubException as e:
        print_pr_guidance(str(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
