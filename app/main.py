from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    # Simple validation example: allow only alphanumeric characters and hyphens
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    return all(char in allowed_chars for char in host)