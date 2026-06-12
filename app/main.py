from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['192.168.1.1', '10.0.0.1']
    if host in allowed_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
        return {'status': 'completed'}
    else:
        return {'status': 'denied', 'message': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)