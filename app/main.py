from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    # Validate host input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Ping failed: {e.stderr}')
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}