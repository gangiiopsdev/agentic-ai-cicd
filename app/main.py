from fastapi import FastAPI
import subprocess
from shlex import quote

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 64:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', quote(host)], check=True, capture_output=True)
    return {'status': 'completed'}