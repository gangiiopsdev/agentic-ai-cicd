from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True to handle errors gracefully
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)