from fastapi import FastAPI
import subprocess
import shlex
def shell_safe(input_string):
    return ''.join(e if e.isalnum() else '_' for e in input_string)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shell_safe(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)
    return {'status': 'completed'}