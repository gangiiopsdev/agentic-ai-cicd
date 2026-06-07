from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str): 
    return safe_ping(host)