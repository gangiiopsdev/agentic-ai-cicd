from fastapi import FastAPI
import subprocess
from typing import List
globally_banned_hosts: List[str] = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_banned_hosts:
        raise ValueError('Host is not allowed')
    subprocess.call(['ping', host])
    return {'status': 'completed'}