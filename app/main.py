from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain potentially harmful characters
    if any(char in host for char in [';', '|', '&', '*', '?', '<', '>', '$', '`']):
        return {'status': 'error', 'error': 'Invalid input'}
    return safe_ping(host)