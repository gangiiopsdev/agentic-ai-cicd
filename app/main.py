from fastapi import FastAPI
import subprocess
import shlex
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex to escape command arguments for command execution
    try:
        subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}