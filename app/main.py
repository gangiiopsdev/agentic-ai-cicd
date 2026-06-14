from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}