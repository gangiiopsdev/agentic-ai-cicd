from fastapi import FastAPI
import subprocess
import shlex
globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts

app = FastAPI()

def sanitize_host(host):
    return host.strip() if host in globally_safe_hosts else None

def validate_input(input_data):
    if not isinstance(input_data, str) or '&&' in input_data or ';' in input_data:
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    try:
        validate_input(host)
        safe_host = sanitize_host(host)
        if safe_host and shlex.split(safe_host) == ['ping', safe_host]:  # Ensure safe_host is not modified to avoid injection
            subprocess.run(['ping', *shlex.split(safe_host)], check=True, capture_output=True)
        return {'status': 'completed'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}