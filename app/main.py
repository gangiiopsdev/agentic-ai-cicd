from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with a full executable path
    subprocess.run(['/usr/bin/ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}