from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split for safe argument splitting
    try:
        args = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}