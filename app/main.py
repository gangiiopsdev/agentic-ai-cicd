from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Add allowed hosts here
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)