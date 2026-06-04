from fastapi import FastAPI
import subprocess
import shlex
from typing import Tuple

global_subprocess = None

def ping(host: str) -> Tuple[bytes, bytes]:
    # Input validation with more strict rules to prevent injection attacks
    if not all(char.isalnum() or char in ['.', '-'] for char in host):
        raise ValueError('Invalid hostname')
    global global_subprocess
    if global_subprocess is not None:
        global_subprocess.terminate()
    args = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return result.stdout, result.stderr

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    try:
        result = ping(host)
        return {'stdout': result[0].decode(), 'stderr': result[1].decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}