from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()
def ping(host: str):    validate_host(host)
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}