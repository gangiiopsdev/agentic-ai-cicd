from fastapi import FastAPI
import subprocess
from typing import Optional
def escape_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in '._-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_input(host)
    try:
        output = subprocess.check_output(['ping', '-c', '4', escaped_host], stderr=subprocess.STDOUT, timeout=10, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}