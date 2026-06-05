from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if 'ping' in host:
        return "Invalid input"
    return subprocess.call(shlex.split('ping ' + host))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int) and result == 0:
        return {"status": "completed", "output": "Ping successful"}
    else:
        return {"status": "failed", "output": "Ping failed"}