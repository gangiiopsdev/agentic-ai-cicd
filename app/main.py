from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['-', '.', '_'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}