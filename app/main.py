from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}