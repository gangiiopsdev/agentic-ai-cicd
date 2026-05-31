from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if host.strip().endswith(('.com', '.net', '.org')):
        subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid hostname")

    return {"status": "completed"}