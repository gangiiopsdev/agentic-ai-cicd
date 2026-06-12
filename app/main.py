from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex to safely split the command string
    cmd = shlex.split(f"ping {host}")
    subprocess.call(cmd)
    return {"status": "completed"}