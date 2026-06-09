from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    try:
        subprocess.run(['ping', '-c 4', host], check=True, shell=False)  # Limit the number of pings to avoid potential abuse
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}