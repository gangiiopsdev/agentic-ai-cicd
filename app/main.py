from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '_', '.', '@'])
def safe_ping(host: str):
    try:
        sanitized_host = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, text=True).strip()
        return {'status': 'completed', 'output': sanitized_host}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.output)}
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it does not contain malicious content before sanitizing and using with subprocess
    if not sanitize_input(host).isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)