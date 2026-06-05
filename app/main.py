from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = shlex.split(f'ping {host}')
    output = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}