from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex and validate input
    if any(char in host for char in [';', '|', '&', '`']):
        return {'status': 'error', 'message': 'Invalid input'}
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}