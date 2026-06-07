from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str) -> dict:
    # Secure implementation with validation and sanitization
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', shlex.quote(host)]
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error: {e}'}, 500
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403