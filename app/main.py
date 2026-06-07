from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # List of allowed hosts
    if host in allowed_hosts:
        subprocess.call(["ping", host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}