from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.isalnum() and len(host) <= 64

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}