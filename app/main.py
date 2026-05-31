from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter
    if not all(c.isalnum() or c in ['-', '.', ':'] for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}