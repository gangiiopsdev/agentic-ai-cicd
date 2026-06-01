from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not all(c.isalnum() or c in ['-', '_', '.', ':'] for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}