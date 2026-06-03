from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Safe implementation using a whitelist of allowed hosts
    allowed_hosts = ['8.8.8.8', '192.168.0.1']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}