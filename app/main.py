from fastapi import FastAPI
import subprocess

app = FastAPI()

def check_host(host):
    if not host:
        raise ValueError('Host parameter is required')
    return host

def ping(host: str):
    host = check_host(host)
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}