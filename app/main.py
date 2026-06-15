from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Safe implementation using subprocess.run with proper quoting and validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}