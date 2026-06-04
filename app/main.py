from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use a whitelist approach for safe input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid input'}
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}