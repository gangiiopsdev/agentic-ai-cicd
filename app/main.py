from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Simple validation: allow only alphanumeric characters and some common delimiters
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        command = f'ping {host}'
        subprocess.call(shlex.split(command))
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Invalid host input'}, 400