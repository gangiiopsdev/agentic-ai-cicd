from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host):
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    if not valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return secure_ping(host)

def valid_host(host):
    # Implement validation logic to ensure the host is safe
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts