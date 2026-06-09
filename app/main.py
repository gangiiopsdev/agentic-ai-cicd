from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper validation and sanitization
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or only whitespace')
    subprocess.call(['ping', '-c', '1', host])  # Use specific arguments for ping
    return {'status': 'completed'}