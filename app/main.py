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
    if not host or len(host) > 100:
        raise ValueError("Invalid host name")
    subprocess.run([os.path.join(os.environ['PATH'], 'ping'), host], check=True)
    return {"status": "completed"}