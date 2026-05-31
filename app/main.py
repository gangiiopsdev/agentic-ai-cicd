from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)