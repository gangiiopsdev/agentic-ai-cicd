from fastapi import FastAPI
import shlex
import subprocess
import re
def safe_ping(host: str):
    try:
        # Use subprocess.run for safer execution and avoid shell=True
        output = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host parameter'}
    return safe_ping(host)