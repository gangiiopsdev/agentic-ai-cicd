from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPHostHeaderParam
def _ping(host: str):
    command = ['ping', host]
    output = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': output.stdout}
app = FastAPI()
@app.get('/ping/{host}')
def ping(host: str = HTTPHostHeaderParam(..., description='Allowed hosts only')):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return _ping(host)