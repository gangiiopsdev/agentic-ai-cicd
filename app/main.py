from fastapi import FastAPI
import subprocess
def execute_ping(host):
    if 'ping' not in host:
        return False
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if execute_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid host parameter"}