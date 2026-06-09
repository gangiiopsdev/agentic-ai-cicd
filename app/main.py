from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    try:
        # Use f-string to safely include host in the command
        result = subprocess.run(['ping', '-c', '1', host], check=True, timeout=5, capture_output=True, shell=False)
        return {
            "status": "completed",
            "result": result.stdout.decode('utf-8')
        }
    except Exception as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a valid IP or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host input"}
    return safe_ping(host)