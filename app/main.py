from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}