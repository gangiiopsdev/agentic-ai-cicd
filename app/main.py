from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using shlex to avoid command injection
    args = shlex.split(f'ping {host}')
    subprocess.run(args)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}