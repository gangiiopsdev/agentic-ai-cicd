from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host or ' ' in host:
        raise ValueError("Invalid host name")

    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}