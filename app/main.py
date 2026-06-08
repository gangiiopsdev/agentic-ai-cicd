from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the input is sanitized to avoid command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}