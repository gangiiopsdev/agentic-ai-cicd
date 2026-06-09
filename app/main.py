from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def execute_ping(host):
    # Validate the host parameter using a regular expression
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host name'
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}