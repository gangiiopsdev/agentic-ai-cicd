from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and shlex.split to avoid shell injection
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}