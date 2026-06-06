from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.strip() or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host parameter'}
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output)}