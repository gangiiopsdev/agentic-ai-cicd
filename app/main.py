from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate the host parameter
    if not host or ' ' in host:
        raise ValueError("Invalid host parameter")
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}