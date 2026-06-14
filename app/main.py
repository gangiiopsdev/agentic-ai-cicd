from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host for ping operation')

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