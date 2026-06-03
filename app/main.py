from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host or not host.strip():
        return {'error': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e.stderr.decode()}'}