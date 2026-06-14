from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    return host in allowed_hosts

def sanitize_input(input_str):
    sanitized = ''.join(e for e in input_str if e.isalnum() or e.isspace())
    return sanitized

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = ['ping', '-c', '1'] + shlex.split(sanitize_input(host))
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}