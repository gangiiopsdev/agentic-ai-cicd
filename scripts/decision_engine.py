import json
import os
import re
import sys

RESPONSE_FILE = "reports/agent_response.json"
DECISION_FILE = "reports/decision.json"

os.makedirs("reports", exist_ok=True)

def load_agent_response(path):
    # Guard 1: file missing or empty
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print(f"⚠️  {path} is missing or empty. Defaulting to safe mode.")
        return None

    with open(path) as f:
        raw = f.read().strip()

    # Guard 2: try direct JSON parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Guard 3: extract JSON from markdown fences ```json ... ```
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    print(f"❌ Could not parse JSON from {path}. Raw content:\n{raw[:500]}")
    return None


result = load_agent_response(RESPONSE_FILE)

# Safe defaults if AI agent failed
if result is None:
    severity = "HIGH"          # fail-safe → require human review
    confidence = 0
else:
    severity = result.get("severity", "HIGH").upper()
    confidence = int(result.get("confidence_score", 0))

auto_fix = False
if severity == "LOW":
    auto_fix = True
elif severity == "MEDIUM" and confidence >= 85:
    auto_fix = True
elif severity == "HIGH":
    auto_fix = False

print(f"Severity: {severity} | Confidence: {confidence} | Auto-fix: {auto_fix}")

with open(DECISION_FILE, "w") as out:
    json.dump({
        "severity": severity,
        "confidence_score": confidence,
        "auto_fix": auto_fix
    }, out, indent=2)

print(f"✅ Decision written to {DECISION_FILE}")
