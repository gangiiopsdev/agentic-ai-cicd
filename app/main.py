from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ' '.join(host.split())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if '@' not in sanitized_host:
        subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}