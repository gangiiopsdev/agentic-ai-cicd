from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}