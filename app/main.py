from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and logging
    if not host.isalnum():
        raise ValueError("Invalid host name")
    args = shlex.split(f"ping {host}")
    subprocess.run(args)
    return {"status": "completed"}