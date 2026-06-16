from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import urlparse

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        sanitized_host = sanitize_host(host)
        cmd = ['ping', sanitized_host]
        args = shlex.split(' '.join(cmd))
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}