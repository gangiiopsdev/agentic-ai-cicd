from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host parameter")
    cmd = shlex.split(f'ping {host}')
    subprocess.run(cmd, check=True, capture_output=True)
    return {"status": "completed"}