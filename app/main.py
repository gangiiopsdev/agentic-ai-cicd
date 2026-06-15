from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['-', '.', '_'])

def validate_host(host: str):
    allowed_hosts = {'example.com', 'test.com'}  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    sanitized_host = quote(sanitize_input(host))
    try:
        output = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}