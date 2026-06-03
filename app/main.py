from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with full path and shell=False to avoid command injection
    result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}