from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host or not host.isalnum():
        raise ValueError('Invalid host name')
    return host

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    subprocess.run(['ping', validated_host], check=True)
    return {'status': 'completed'}