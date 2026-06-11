from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' in host:
        return "Invalid input"
    return subprocess.call(['ping', host], timeout=5, shell=False)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping failed"}