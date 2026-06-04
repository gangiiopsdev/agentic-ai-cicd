from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent code injection
    if not host.isdigit() or len(host) != 3:
        raise ValueError("Invalid host address")
    subprocess.call(["ping", host])
    return {"status": "completed"}