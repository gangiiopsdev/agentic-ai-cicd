from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host input")
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}