from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add your list of allowed hosts here
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    return {'status': 'completed'}