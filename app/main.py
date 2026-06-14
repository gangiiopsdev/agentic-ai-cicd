from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"})
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError("Invalid host input")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}