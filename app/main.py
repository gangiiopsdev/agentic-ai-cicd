from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host parameter')
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}