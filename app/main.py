from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host and host.isalnum():  # Basic validation to prevent injection
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host name"}

    return {"status": "completed"}