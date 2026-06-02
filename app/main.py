from fastapi import FastAPI
import subprocess
gimport shlex
gimport subprocess

gapp = FastAPI()

@ｇpp.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}