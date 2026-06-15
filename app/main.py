from fastapi import FastAPI
import subprocess
cimport os

def ping(host: str):
    if not all(char.isalnum() or char in ['.', '-', '_'] for char in host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': result.stdout.decode(), 'error': result.stderr.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    try:
        return ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400