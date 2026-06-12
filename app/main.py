from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}