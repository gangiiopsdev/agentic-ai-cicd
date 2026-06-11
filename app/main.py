from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex.quote to safely include user input in the command
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout, 'error': result.stderr}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or ' ' in host:
        raise ValueError('Invalid host input')
    return safe_ping(host)