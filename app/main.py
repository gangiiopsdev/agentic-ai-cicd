from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_result = safe_ping(host)
    if safe_ping_result == 0:
        return {"status": "completed", "output": "Ping successful"}
    else:
        return {"status": "failed", "output": "Ping failed"}