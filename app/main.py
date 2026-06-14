from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation, should be more robust in production
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', f'--{host}'], check=True, shell=False)
    return {'status': 'completed'}