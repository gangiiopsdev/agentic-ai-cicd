from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isdigit():
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
    return {"status": "completed"}