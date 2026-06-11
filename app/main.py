from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_hostname(hostname):
    return bool(re.match(r'^[a-zA-Z0-9-.:_]+$', hostname))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        cmd = ['ping', '-c', '1', shlex.quote(host)]
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}