from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host format"}
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}