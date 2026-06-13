from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Use subprocess.run with shell=False to prevent shell injection
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}
def sanitize_input(host):
    # Sanitize input to prevent injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if all(char in allowed_chars for char in host) and len(host.split('.')) == 2:
        return host
    else:
        raise ValueError('Invalid host')
@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        if validate_host(sanitized_host):
            # Use subprocess.run with shell=False to prevent shell injection
            result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'message': 'Invalid host'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}