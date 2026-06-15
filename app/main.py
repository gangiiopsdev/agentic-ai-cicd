from fastapi import FastAPI
import subprocess
import shlex
global pids = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    pid = subprocess.Popen(['ping', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pids[safe_host] = pid.pid
    return {"status": "completed", "pid": pid.pid}