from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host or 'ping' in host:
        raise ValueError('Invalid input for ping')
    subprocess.call(['ping', host])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400
    return {'status': 'completed'}