from fastapi import FastAPI
import subprocess
import shlex

host_whitelist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in host_whitelist:
        command = ['ping', *shlex.split(host)]
        subprocess.run(command, check=True)
    else:
        raise ValueError('Unauthorized host')
    return {'status': 'completed'}