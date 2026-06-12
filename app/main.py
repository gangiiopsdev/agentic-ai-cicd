from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

def validate_host(host):
    if not host or not host.isalnum():
        return False
    return True

@global_app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}