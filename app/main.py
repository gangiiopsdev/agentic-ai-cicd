from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = ['ping', host]
    output = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if output.returncode != 0:
        return {'status': 'failed', 'error': output.stderr}
    return {'status': 'completed', 'output': output.stdout}