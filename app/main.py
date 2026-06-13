from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip().isdigit() and '@' not in host:
        args = shlex.split(f'ping -c 1 {host}')
        subprocess.run(args, check=True, capture_output=True)
    else:
        return {"error": "Invalid input"}

    return {"status": "completed"}