from fastapi import FastAPI
import subprocess
import shlex
globally_safe_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in globally_safe_hosts:
        raise ValueError('Invalid host')
    args = ['ping', *shlex.split(host)]  # Use shlex to safely split the command line
    subprocess.run(args, check=True)  # Use subprocess.run with shell=False and check=True for better security
    return {'status': 'completed'}