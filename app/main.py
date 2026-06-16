from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Change method name to avoid conflict with built-in 'ping'
    try:
        allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
        if host not in allowed_hosts:
            raise ValueError('Host not allowed')
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}