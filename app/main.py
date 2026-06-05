from fastapi import FastAPI
import subprocess
c import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    valid_hosts = ["example.com", "localhost"]  # Example validation logic
    return host in valid_hosts