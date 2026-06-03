from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}