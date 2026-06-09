from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with full path to ensure no shell injection
    subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True)
    return {"status": "completed"}