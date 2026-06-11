from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation for host
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host"}, 400
    subprocess.call(["ping", host])

    return {"status": "completed"}