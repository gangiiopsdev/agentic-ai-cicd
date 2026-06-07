from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Validate hostname
    if not host.isalnum() or '.' in host:
        return {'error': 'Invalid hostname'}
    # Use shlex to safely quote the command arguments
    args = shlex.split('ping') + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)