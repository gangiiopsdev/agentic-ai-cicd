from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent injection attacks
    if not host or not host.isalnum() or ' ' in host:
        raise ValueError("Invalid host name")
    # Secure implementation using subprocess.run with shlex.split for safe command argument parsing
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}