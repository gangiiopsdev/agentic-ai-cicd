from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Ping failed: {result.stderr}")

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping_fixed(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Ping failed: {result.stderr}")
    return {"status": "completed"}