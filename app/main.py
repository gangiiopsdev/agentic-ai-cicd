from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    allowed_hosts = ['example.com', '127.0.0.1']  # Example whitelist
    if host in allowed_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}