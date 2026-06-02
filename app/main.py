from fastapi import FastAPI
import subprocess
import shlex
from typing import List

app = FastAPI()

allowed_hosts: List[str] = ['example.com', 'test.com']

def escape_shell_arg(arg):
    return shlex.quote(arg)

def is_host_allowed(host: str) -> bool:
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    if not is_host_allowed(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(['ping', escape_shell_arg(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}