from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', '127.0.0.1']  # Define allowed hosts
    return host in allowed_hosts

cmd = ['/bin/ping', '-c', '4', host]
subprocess.run(cmd, check=True, capture_output=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return {'status': 'completed'}