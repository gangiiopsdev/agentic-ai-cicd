from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input here to ensure it is safe
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}

    safe_host = shlex.quote(host)
    subprocess.call(['ping', '-c', '1', safe_host])
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)