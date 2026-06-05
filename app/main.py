from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['localhost', '127.0.0.1']:
        return True
    return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400