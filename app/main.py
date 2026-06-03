from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host name')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}