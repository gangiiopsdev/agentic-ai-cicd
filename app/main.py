from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run with a list of arguments for safety and validate input
    if not host or ' ' in host:
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}