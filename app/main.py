from fastapi import FastAPI
import subprocess
from shlex import quote as q
from pathlib import Path

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '-_.:/\=' else '_' for c in arg)

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter cannot be empty'}
    try:
        escaped_host = escape_shell_arg(host)
        output = subprocess.check_output(['ping', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}