from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and escaping
    if not host.strip() or '<' in host or '>' in host:
        raise ValueError('Invalid host input')
    command_parts = shlex.split(f'ping -c 1 {host}')
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}