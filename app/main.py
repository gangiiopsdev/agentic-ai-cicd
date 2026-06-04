from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']

def is_valid_host(host: str) -> bool:
    return any(host.endswith(allowed_host) for allowed_host in ALLOWED_HOSTS)

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}