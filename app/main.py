from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

# Secure version using parameterized command execution
def ping_secure(host: str):
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

app.get('/ping_secure')
def ping_secure_route(host: str):
    return ping_secure(host)