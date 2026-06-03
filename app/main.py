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
    global_subprocess = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return global_subprocess.communicate()

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    result = ping(host)
    return {'stdout': result[0].decode(), 'stderr': result[1].decode()}