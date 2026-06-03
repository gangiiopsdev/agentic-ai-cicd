from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}