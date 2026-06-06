from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate host to prevent injection attacks
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid input'}
        cmd = ['ping', host]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}