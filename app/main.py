from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)

    return {"status": "completed"}