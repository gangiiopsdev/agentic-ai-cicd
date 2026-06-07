from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    pattern = r'^[a-zA-Z0-9]{1,255}$'
    return re.match(pattern, input_str) is not None

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        args = shlex.split('ping') + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}