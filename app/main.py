from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with proper input sanitization
    if not host.strip().isdigit() or '.' not in host:
        raise ValueError('Invalid host parameter')
    args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to prevent DoS attacks
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}