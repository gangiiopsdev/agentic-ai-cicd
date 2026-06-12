from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.strip():
        return False
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        return False
    subprocess.call(['ping', host])
    return True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid host"}