from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}