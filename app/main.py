from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPHostHeaderParam

app = FastAPI()

async def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/ping/{host}')
def ping(host: str = HTTPHostHeaderParam(..., description='Allowed hosts only')):
    validate_host(host)
    command = ['ping', host]
    output = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': output.stdout}