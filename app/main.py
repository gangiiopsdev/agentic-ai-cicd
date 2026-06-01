from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    try:
        ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}