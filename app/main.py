from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host.isnumeric() or int(host) < 1 or int(host) > 254:
        raise ValueError("Invalid host value")
    subprocess.call(["ping", host])
    return {"status": "completed"}