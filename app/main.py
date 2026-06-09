from fastapi import FastAPI
import subprocess
from shlex import quote
from os import path
current_dir = path.dirname(path.abspath(__file__))
app = FastAPI()
def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    subprocess.call([path.join(current_dir, 'ping'), quote(host)])