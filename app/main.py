from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'another.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', shlex.quote(host)], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')