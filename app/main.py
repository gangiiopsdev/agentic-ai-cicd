from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the user input
    if not re.match(r'^\d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}$', host):
        return {"status": "failed", "error": "Invalid IP address"}

    try:
        # Use whitelist for allowed hosts or IP ranges
        if host not in ['192.168.1.1', '10.0.0.1']:  # Replace with actual whitelist logic
            return {"status": "failed", "error": "Host not allowed"}
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive Controls
# 1. Validate and sanitize the user input
# 2. Use whitelisting for allowed hosts or IP ranges
# 3. Log all subprocess calls for auditing purposes