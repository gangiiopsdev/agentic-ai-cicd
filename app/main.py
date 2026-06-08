from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious commands
    if any(char in host for char in [';', '|', '&', '<', '>', '`']):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run([quote('ping'), quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}