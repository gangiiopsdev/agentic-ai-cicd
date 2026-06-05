from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote and input validation
    if not host.strip().isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}')))
    return {"status": "completed"}