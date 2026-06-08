from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Define allowed hosts
    return host in allowed_hosts

def sanitize_host(host):
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in ('-', '.', ':'))
    return sanitized_host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if validate_host(sanitized_host):  # Validate and sanitize the input
        command = ['ping', sanitized_host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}