from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host or not host.strip():
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}