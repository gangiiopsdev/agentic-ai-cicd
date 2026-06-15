from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> str:
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        command = 'ping {}'.format(shlex.quote(host))
        try:
            subprocess.run(command, check=True, shell=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)