from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', '-c 1', host], shell=False)
    else:
        raise ValueError('Invalid host specified')

    return {'status': 'completed'}