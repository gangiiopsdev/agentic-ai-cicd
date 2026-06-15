from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to avoid shell injection
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}