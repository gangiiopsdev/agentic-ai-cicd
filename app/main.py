from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e == '.' or e == '-').strip()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize and validate the host input
        sanitized_host = sanitize_input(host)
        if not sanitized_host:
            raise ValueError('Invalid host input')
        command_parts = ['ping', '-c', '1', shlex.quote(sanitized_host)]
        output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}