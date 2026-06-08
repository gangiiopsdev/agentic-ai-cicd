from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping --no-host-alias --non-privileged {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}