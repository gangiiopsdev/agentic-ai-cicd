from fastapi import FastAPI
import subprocess
import shlex

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host'}, 400
    command = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(command, check=True, timeout=5)
    return {'status': 'completed'}