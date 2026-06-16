from fastapi import FastAPI
import subprocess
from typing import Set
global pings: Set[str] = set()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in {'192.168.1.1', '10.0.0.1'}:
        subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}