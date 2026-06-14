from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', host]
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    result = safe_ping(host)
    return result
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    return host in allowed_hosts