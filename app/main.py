from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c.isdigit())
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c.isdigit())
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}