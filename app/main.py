from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def execute_ping(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        args = ['ping', host]
        subprocess.call(args, shell=False)
    else:
        raise ValueError('Invalid input for host')

@app.get('/ping')
def ping(host: str):
    try:
        execute_ping(host)
    except Exception as e:
        return {'error': str(e)}