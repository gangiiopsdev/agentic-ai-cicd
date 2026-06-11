from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_input(input_string):
    if not re.match(r'^[a-zA-Z0-9\s]*$', input_string):
        raise ValueError('Invalid input detected')

def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

@app.get('/ping')
def ping(host: str):
    validate_input(host)
    command_parts = ['ping', *shlex.split(host)]
    return run_safe_command(command_parts)