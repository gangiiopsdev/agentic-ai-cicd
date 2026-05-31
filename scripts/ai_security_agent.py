import json
import os
import re
import sys
from litellm import completion

REPORTS_DIR = "reports"
OUTPUT_FILE = f"{REPORTS_DIR}/agent_response.json"
BANDIT_FILE = "bandit-report.json"
SOURCE_FILE = "app/main.py"

os.makedirs(REPORTS_DIR, exist_ok=True)


def safe_read_json(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print(f"⚠️  {path} missing or empty")
        return {}
    try:
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"⚠️  Could not parse {path}: {e}")
        return {}


def safe_read_file(path):
    if not os.path.exists(path):
        print(f"⚠️  {path} not found")
        return ""
    with open(path) as f:
        return f.read()


def extract_json(text):
    """Extract JSON object from LLM response (handles ```json fences)."""
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Extract from markdown code fence
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        try:
            return json.loads(fence.group(1))
        except json.JSONDecodeError:
            pass

    # Fallback: grab first {...} block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    return None


def write_fallback(reason):
    """Write a safe default response so downstream steps never crash."""
    fallback = {
        "severity": "HIGH",
        "confidence_score": 0,
        "auto_remediation_allowed": False,
        "summary": f"AI agent failed: {reason}",
        "fixed_code": "",
        "recommendations": ["Manual review required."]
    }
    with open(OUTPUT_FILE, "w") as f:
        json.dump(fallback, f, indent=2)
    print(f"⚠️  Wrote fallback response to {OUTPUT_FILE}")


# ---------- Main ----------
findings = safe_read_json(BANDIT_FILE)
vulnerable_code = safe_read_file(SOURCE_FILE)

if not findings and not vulnerable_code:
    write_fallback("No bandit findings or source code found")
    sys.exit(0)

prompt = f"""
You are a senior DevSecOps AI agent.

Analyze this vulnerable Python application.

Tasks:
1. Explain the vulnerability
2. Classify severity (LOW, MEDIUM, HIGH)
3. Estimate remediation confidence score (0-100)
4. Determine if auto-remediation is safe
5. Generate secure fixed code
6. Suggest preventive controls

IMPORTANT: Respond with ONLY a valid JSON object. No markdown, no explanations outside JSON.

Security Findings:
{json.dumps(findings, indent=2)}

Source Code:
{vulnerable_code}

Return EXACTLY this JSON structure:
{{
  "severity": "LOW|MEDIUM|HIGH",
  "confidence_score": 0,
  "auto_remediation_allowed": true,
  "summary": "",
  "fixed_code": "",
  "recommendations": []
}}
"""

try:
    response = completion(
        model="ollama/qwen2.5-coder",
        messages=[{"role": "user", "content": prompt}],
        api_base="http://localhost:11434",
        timeout=300
    )
    raw_output = response['choices'][0]['message']['content']
    print("=== Raw LLM Output ===")
    print(raw_output[:500])
    print("======================")

    parsed = extract_json(raw_output)
    if parsed is None:
        write_fallback("LLM returned invalid JSON")
        sys.exit(0)

    # Normalize severity casing
    parsed["severity"] = parsed.get("severity", "HIGH").upper()
    parsed["confidence_score"] = int(parsed.get("confidence_score", 0))

    with open(OUTPUT_FILE, "w") as f:
        json.dump(parsed, f, indent=2)

    print(f"✅ AI security analysis written to {OUTPUT_FILE}")

except Exception as e:
    print(f"❌ AI agent error: {e}")
    write_fallback(str(e))
    sys.exit(0)   # Don't fail the pipeline — let decision engine handle it
