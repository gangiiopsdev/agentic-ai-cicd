from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitize_host(host)
    subprocess.call(f"ping {host}")
    return {"status": "completed"}