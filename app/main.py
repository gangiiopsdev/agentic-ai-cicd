from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.call(f"ping {host}", shell=True)
    return {"status": "completed"}