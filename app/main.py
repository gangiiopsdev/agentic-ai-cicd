from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}