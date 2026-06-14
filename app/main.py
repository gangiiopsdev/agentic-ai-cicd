from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if not host.strip():
        return {"error": "Invalid host parameter"}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}