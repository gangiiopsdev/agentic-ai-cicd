from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess_call(command: str) -> None:
    args = shlex.split(command)
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_subprocess_call(f'ping {host}')
    return {"status": "completed"}