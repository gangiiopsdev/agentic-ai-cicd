from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host format')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}