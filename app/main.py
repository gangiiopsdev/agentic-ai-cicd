from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

global_ping_command = 'ping'

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str) -> Union[dict, dict]:
    if validate_host(host):
        try:
            subprocess.call([global_ping_command, host])
        except Exception as e:
            return {'error': str(e)}
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}