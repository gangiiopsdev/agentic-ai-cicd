from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a whitelist of allowed hosts
    allowed_hosts = ["127.0.0.1", "192.168.1.1"]  # Example list
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}