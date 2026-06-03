from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and not all(c in '0123456789.-' for c in host):
        raise ValueError("Invalid host name")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}