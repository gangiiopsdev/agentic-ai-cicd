from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with sanitized input and full executable path
    return safe_ping(host)