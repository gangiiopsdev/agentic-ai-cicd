from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Use shlex.quote to safely handle the host input
    quoted_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', quoted_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input further to ensure it does not contain malicious content
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid or malicious input'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not host or any(char not in allowed_chars for char in host):
        return False
    return True