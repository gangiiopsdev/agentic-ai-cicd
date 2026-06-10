from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate and sanitize the host parameter
    if not host.replace('.', '').isnumeric() or '.' not in host:
        raise ValueError("Invalid host format")
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}