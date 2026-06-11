from fastapi import FastAPI
import subprocess
import shlex
import os
global app
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    valid_hosts = ["google.com", "example.com"]  # Replace with actual validation logic
    return host in valid_hosts