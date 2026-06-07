from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def execute_command(command_parts):
    try:
        output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=5)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    valid_host_pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not valid_host_pattern.match(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    command_parts = ['ping', '-c', '1'] + shlex.split(host)
    success, output = execute_command(command_parts)
    if success:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': output}