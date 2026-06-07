from fastapi import FastAPI
import subprocess
import re
import shlex
def sanitize_host(host: str) -> str:
    return re.sub(r'[^a-zA-Z0-9.-]', '', host)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Validate input
    if not sanitized_host:
        return {'error': 'Invalid host parameter'}
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output)}