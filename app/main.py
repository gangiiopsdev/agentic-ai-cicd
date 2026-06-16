from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper quoting
    if not host.isalnum():
        raise ValueError("Invalid input")
    command = shlex.split(f'ping -c 1 {shlex.quote(host)}')
    subprocess.call(command)
    return {"status": "completed"}