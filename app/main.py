from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with full path and input validation
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call([os.path.join(os.getcwd(), 'ping'), host])
    return {"status": "completed"}