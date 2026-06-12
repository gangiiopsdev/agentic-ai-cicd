from fastapi import FastAPI
import subprocess
import shlex
import shlex

app = FastAPI()

def validate_host(host):
    if not host.strip().startswith('192.168.'):
        raise ValueError("Invalid host")

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}