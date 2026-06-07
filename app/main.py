from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError("Invalid host name")
    subprocess.call(["ping", host])
    return {"status": "completed"}