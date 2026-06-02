from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.split
    command_parts = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}