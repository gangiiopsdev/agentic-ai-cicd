from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}