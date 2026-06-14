from fastapi import FastAPI
import subprocess
import re

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
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}