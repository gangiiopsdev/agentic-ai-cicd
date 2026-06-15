from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric() or '.' in host:
        return True
    else:
        return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host for ping')
    return {'status': 'completed'}