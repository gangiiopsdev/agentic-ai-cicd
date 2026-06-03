from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid input. Only alphanumeric characters are allowed.')
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}