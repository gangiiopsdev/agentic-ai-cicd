from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e == '.').rstrip('.')[:255]

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}