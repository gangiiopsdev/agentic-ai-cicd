from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}