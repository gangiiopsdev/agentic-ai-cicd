from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split('ping ' + host)
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)