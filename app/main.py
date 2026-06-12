from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def ping(host: str) -> dict:
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    command = f'ping {host}'
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}