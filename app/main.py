from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}