from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input
        if not host or len(host) > 255 or not all(c.isalnum() or c in '.-_' for c in host):
            return {"status": "failed", "error": "Invalid host"}

        # Using check_output instead of call and avoiding shell=True for security
        result = subprocess.check_output(['ping', '-c 4', host], timeout=10, stderr=subprocess.STDOUT)
        return {"status": "completed", "result": result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}