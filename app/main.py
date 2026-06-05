from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    result = subprocess.run(command, check=True)
    return {'status': 'completed'}