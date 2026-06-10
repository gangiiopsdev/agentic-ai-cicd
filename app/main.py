from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isdigit():
        raise ValueError("Invalid host")
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}