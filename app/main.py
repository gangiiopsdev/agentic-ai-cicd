from fastapi import FastAPI
import subprocess
global pids = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pid = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pids[host] = pid.pid
    return {"status": "completed", "pid": pid.pid}