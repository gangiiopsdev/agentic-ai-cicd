from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Sanitize the input to prevent shell injection
    if not host.strip().isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}