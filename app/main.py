from fastapi import FastAPI
import subprocess

app = FastAPI()

def check_host(host):
    if not host:
        raise ValueError('Host parameter is required')
    return host

@app.get('/ping')
def ping(host: str):
    host = check_host(host)
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}