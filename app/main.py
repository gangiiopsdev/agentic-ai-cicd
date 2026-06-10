from fastapi import FastAPI
import subprocess
from typing import List

global ping_safe_hosts
ping_safe_hosts: List[str] = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in ping_safe_hosts:
        subprocess.call(['ping', '-c', '4', host])
    else:
        return {'error': 'Unauthorized host'}, 403

    return {'status': 'completed'}