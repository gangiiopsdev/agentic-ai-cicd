from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}

    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}