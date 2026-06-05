from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote as cmd_quote

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.strip()

@app.get('/ping')
def ping(host: str):
    if not host or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    # Use safe method for executing commands without shell=True
    command = shlex.split('ping {}'.format(cmd_quote(sanitized_host)))
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}