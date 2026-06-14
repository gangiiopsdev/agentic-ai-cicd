from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'Invalid hostname'}
    return {'status': safe_ping(host)}