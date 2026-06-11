from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call for better control and safety
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    # Add additional validation and sanitization
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None