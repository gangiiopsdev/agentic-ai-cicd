from fastapi import FastAPI
import shlex
import subprocess
gapp = FastAPI()

@ｇpp.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}