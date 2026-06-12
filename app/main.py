from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    if not re.match(r'^[a-zA-Z0-9.-]+$', input_string):
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        args = shlex.split('ping -c 4 ' + host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}