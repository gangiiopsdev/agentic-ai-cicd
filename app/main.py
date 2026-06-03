from fastapi import FastAPI
import subprocess
import shlex

global app, host
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    safe_host = shlex.quote(host)
    subprocess.call(shlex.split(f'ping {safe_host}'))
    return {"status": "completed"}