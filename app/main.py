from fastapi import FastAPI
import subprocess
import shlex
global host_list
host_list = ['192.168.0.1', '192.168.0.2']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):,
    if host in host_list:
        subprocess.call(shlex.split('ping ' + host))
        return {'status': 'completed'}
    else:
        return {'error': 'Unauthorized host', 'status': 'failed'}