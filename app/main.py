from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():
        raise ValueError("Invalid host")
    # Safe implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}