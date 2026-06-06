from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    executable_path = "/bin/ping"
    subprocess.run([executable_path, host], check=True, capture_output=True)
    return {"status": "completed"}