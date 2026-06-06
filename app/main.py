from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host == 'localhost' or host == '127.0.0.1':
        return subprocess.call(['ping', '-c', '4', host])
    else:
        return -1

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Invalid host for ping"}