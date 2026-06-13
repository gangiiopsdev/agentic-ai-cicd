from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.isdigit():
        return False
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "error": "Invalid host"}
    return {"status": "completed"}