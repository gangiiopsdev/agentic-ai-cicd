from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_input(host):
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}