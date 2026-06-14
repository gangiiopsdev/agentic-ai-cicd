from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_string if char in allowed_chars)

def is_safe_host(host: str):
    safe_hosts = ['example.com', 'localhost']  # Replace with a list of safe hosts
    return host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid or unsafe host')
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}