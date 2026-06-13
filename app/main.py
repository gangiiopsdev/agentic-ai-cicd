from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.call with shell=False and proper input validation
    if host and all(c.isalnum() or c in ['.', '-'] for c in host):
        subprocess.call(["ping", host], shell=False)
    else:
        raise ValueError("Invalid host name")

    return {"status": "completed"}