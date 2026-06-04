from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate host input to ensure it does not contain unexpected characters
        if not host.strip().isalnum():
            return {'error': 'Invalid input'}
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}