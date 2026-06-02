from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        output = subprocess.check_output([quote('ping'), quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

def is_valid_host(host: str) -> bool:
    # Simple example of validation logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts