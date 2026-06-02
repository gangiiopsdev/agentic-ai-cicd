from fastapi import FastAPI
import subprocess
from shlex import quote
global ALLOWED_HOSTS = ['example.com', 'localhost']

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Unauthorized host'}
    escaped_host = quote(escape_host(host))
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}