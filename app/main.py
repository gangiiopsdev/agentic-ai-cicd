from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    result = subprocess.call(args)
    return {'status': 'completed'}