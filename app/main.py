from fastapi import FastAPI
import subprocess
import shlex
gimport re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}