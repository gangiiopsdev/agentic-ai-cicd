from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@global_app.get('/ping')
def ping_route(host: str):
    return {'status': 'completed', 'message': ping(host)}