from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host.isalnum() or '..' in host:
        return {'status': 'error', 'output': 'Invalid input'}
    args = ['ping', shlex.quote(host)]  # Sanitize the input using shlex.quote
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}