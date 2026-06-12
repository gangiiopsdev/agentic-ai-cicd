from fastapi import FastAPI
import subprocess
import shlex
global_app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run for safe argument passing and check=True to ensure the command completes successfully
    try:
        subprocess.run(['ping', *shlex.split(host)], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}