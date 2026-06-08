from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def is_valid_host(host):
    if not host.isalnum() or len(host) > 64:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', '-c', '1', os.path.join(os.getcwd(), host)])
    return {'status': 'completed'}