from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'Invalid input'}
    subprocess.call(f'ping {quote(host)}')
    return {'status': 'completed'}