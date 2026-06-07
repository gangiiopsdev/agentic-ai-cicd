from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate input to ensure it does not contain malicious characters
    if any(char in host for char in [';', '&', '|', '`', '$']):
        raise ValueError('Invalid input')
    args = shlex.split(f'ping {host}')  # Use f-string to avoid shell=True
    subprocess.run(args, check=True)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400
    return {'status': 'completed'}