from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Use a whitelist of allowed hosts or validate the input
    if host not in ['example.com', 'localhost']:
        return {'error': 'Invalid host'}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}