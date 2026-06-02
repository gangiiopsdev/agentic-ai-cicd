from fastapi import FastAPI
import subprocess
import shlex
import re

def safe_ping(host: str):
    # Regular expression to allow only alphanumeric characters and periods
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)