from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}