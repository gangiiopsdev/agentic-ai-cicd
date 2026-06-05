from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    return host.isalnum() and '-' not in host

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid input'}, 400
    command = ['ping', '127.0.0.1'] + shlex.split(host)
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}