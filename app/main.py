from fastapi import FastAPI
import subprocess
import shlex
global app
global ping

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}