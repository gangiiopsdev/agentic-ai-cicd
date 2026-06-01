from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}