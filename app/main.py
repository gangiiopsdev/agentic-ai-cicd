from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts