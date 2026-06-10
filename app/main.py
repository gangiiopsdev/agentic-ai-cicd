from fastapi import FastAPI
import subprocess
import shlex

global host
host = '127.0.0.1' # Set a default safe value for demonstration purposes

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str = host):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {'status': 'completed'}