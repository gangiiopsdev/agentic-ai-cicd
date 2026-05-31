from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to avoid excessive resource usage
    subprocess.run(args, check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)