from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", host])
    return {"status": "completed"}