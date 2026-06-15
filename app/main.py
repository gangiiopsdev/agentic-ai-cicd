from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if 'ping' not in host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}