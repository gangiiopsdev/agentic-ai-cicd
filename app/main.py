from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Enhanced validation to prevent OS command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    cimport = ['ping', host]
    result = subprocess.run(cimport, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    # Validate host to prevent OS command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    return ping(host)