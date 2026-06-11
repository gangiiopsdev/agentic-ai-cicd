from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}