from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it with subprocess
    if not host or not isinstance(host, str) or ' ' in host:
        raise ValueError("Invalid host")
    # Use a safe command and avoid passing user-supplied data directly to the shell
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}