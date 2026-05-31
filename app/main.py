from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and shell=False
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}