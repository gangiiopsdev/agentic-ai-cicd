from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}