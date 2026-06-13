from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    return re.sub(r'[^a-zA-Z0-9 .]', '', input_str)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {shlex.quote(sanitized_host)}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}