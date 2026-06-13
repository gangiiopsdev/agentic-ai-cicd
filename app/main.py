from fastapi import FastAPI
import subprocess
import shlex

global_config = {'ping': '/bin/ping'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = global_config.get('ping', '/bin/ping')
    args = shlex.split(f'{command} {host}')
    try:
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}