from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Add your sanitization logic here, e.g., regex validation
    return input_string.strip()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', '-c', '1', sanitized_host])  # Limit the number of pings
    return {'status': 'completed'}