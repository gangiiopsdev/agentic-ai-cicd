from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

def ping(host: str):
    if host in ALLOWED_HOSTS:
        subprocess.run(['ping', '-c', '1', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}