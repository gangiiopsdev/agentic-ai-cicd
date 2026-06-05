from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)