from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if not host or len(host) > 100:
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '4', host], check=True)
    return {"status": "completed"}