from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host name"}
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "result": result.stdout}