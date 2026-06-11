from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        command = ['ping', *shlex.split(host)]
        output = subprocess.run(command, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Ping command timed out'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}