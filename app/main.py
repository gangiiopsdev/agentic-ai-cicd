from fastapi import FastAPI
import subprocess
global host_validator
host_validator = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

app = FastAPI()

def validate_host(host):
    for char in host:
        if char not in host_validator:
            return False
    if len(host) > 255:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}