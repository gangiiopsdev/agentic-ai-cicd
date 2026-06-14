from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum())

def execute_command(command, args):
    try:
        sanitized_args = [shlex.quote(arg) for arg in args]
        output = subprocess.check_output([command] + sanitized_args, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError('Invalid input for host')
    return execute_command('ping', [sanitized_host])