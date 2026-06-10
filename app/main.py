from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return
    # Use a whitelist of allowed hosts for security
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}