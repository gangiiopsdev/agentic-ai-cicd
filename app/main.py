from fastapi import FastAPI
import subprocess
import shlex

callable_ping = lambda host: subprocess.call(shlex.split(f'ping {host}'))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.call(callable_ping(host))
    return {'status': 'completed'}