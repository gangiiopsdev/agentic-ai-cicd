from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and escaping
    if not host.isalnum():
        raise ValueError("Invalid input")
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}