from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid input")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}