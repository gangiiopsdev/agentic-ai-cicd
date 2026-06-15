from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in ('.', '-', '_'))

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        sanitized_host = shlex.quote(sanitize_input(host))
        output = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'error': output.stderr}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}