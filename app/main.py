from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent shell injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {"status": "denied", "message": "Host is not allowed"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)