from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum() or '>' in host or ';' in host:
        return {'status': 'error', 'message': 'Invalid host'}
    return safe_ping(host)