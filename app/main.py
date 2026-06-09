from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip().isalnum() and '-' not in host:
        raise ValueError("Invalid host parameter")
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}