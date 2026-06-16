from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = ['ping', '-c', '1', shlex.quote(host)]  # Use ping with count to avoid unexpected behavior
    subprocess.run(args, check=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)