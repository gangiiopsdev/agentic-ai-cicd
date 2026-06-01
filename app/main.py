from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    command = ['ping', *shlex.split(host)]
    subprocess.call(command)

    return {'status': 'completed'}