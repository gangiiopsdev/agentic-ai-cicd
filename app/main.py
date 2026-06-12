from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True)
    return {'status': 'completed'}