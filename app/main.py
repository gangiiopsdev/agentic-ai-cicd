from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and list arguments
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid characters in hostname')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}