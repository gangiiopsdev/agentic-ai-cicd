from fastapi import FastAPI
import subprocess

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'error': 'Unauthorized host'}, 403

    # Secure implementation with input sanitization
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', '-c 1', sanitized_host])