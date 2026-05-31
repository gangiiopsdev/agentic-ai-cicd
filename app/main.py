from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return shlex.quote(host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    args = shlex.split(f'ping {escaped_host}')
    subprocess.call(args)

    return {'status': 'completed'}