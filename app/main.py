from fastapi import FastAPI
import subprocess
import shlex
global_app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.quote for safe argument passing
    command = ['ping', *shlex.split(host)]
    subprocess.call(command)
    return {'status': 'completed'}