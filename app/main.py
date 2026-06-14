from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_string if char in allowed_chars)

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    host = sanitize_input(host)  # Sanitize the input before validation
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = ['ping', '-c 1', host]  # Limit the number of pings to avoid abuse
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed'} if result.returncode == 0 else {'status': 'failed', 'error': result.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}