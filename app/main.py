from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError("Host parameter is required")
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}