from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(shlex.split(f'ping {host}'), shell=False)
    return {"status": "completed"}