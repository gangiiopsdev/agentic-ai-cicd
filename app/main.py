from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    result = subprocess.run(command, check=True)
    return {'status': 'completed'}