from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it in subprocess
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid input for host")
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}