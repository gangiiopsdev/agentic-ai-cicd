from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Host not allowed')

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}