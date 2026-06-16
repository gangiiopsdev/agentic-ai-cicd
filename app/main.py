from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with absolute path and validation of input
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host format")
    subprocess.run(["/bin/ping", host], check=True)
    return {"status": "completed"}