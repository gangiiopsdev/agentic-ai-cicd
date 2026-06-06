from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host):
    if host in ('localhost', '127.0.0.1'):
        return subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        raise ValueError('Unsafe host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except ValueError as e:
        return {'error': str(e)}