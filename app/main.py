from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host parameter")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}