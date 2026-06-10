from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Restrict allowed hosts
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}
    else:
        raise Exception('Invalid host')