from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with shell=False to prevent command injection and validate input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host"}, 400
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}