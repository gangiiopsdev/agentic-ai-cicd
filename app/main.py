from fastapi import FastAPI
import subprocess

gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}