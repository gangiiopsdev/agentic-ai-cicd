from fastapi import FastAPI
import shlex
cimport subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {'status': 'completed'}