from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    return safe_ping(host)