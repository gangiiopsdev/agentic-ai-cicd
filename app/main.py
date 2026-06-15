from fastapi import FastAPI
import subprocess
from typing import Set
global pings: Set[str] = set()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in pings:
        pings.add(host)
        # Use a whitelist of allowed hosts or validate the input more strictly
        subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}