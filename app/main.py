from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}