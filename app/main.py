from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/"})
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}