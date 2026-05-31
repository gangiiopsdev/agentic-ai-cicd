from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    args = shlex.split(f'ping {host}')
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {'status': 'failed', 'error': error.decode()}
    return {'status': 'completed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)