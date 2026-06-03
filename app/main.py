from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not validate_host(host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', quote(host)], check=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Simple validation example, replace with more comprehensive validation logic
    return all(c.isalnum() or c in ['.', '-'] for c in host)