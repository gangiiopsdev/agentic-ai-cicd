from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').isdigit():
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}