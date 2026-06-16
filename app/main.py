from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex to safely construct the command
    safe_host = shlex.quote(host)
    subprocess.call(f"ping {safe_host}")
    return {"status": "completed"}