from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Ping to external hosts is not allowed')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}