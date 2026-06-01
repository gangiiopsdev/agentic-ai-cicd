from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        safe_args = shlex.split('ping -c 1 ' + host)
        subprocess.run(safe_args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400