from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '&&' in host or ';' in host:
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', f'127.0.0.1'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}