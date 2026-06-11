from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}