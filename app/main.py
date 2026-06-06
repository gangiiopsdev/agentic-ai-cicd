from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isdigit():
        raise ValueError("Invalid input for host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}