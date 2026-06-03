from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        allowed_hosts = ['example.com', 'test.com']
        if value not in allowed_hosts:
            raise ValueError('Host is not allowed')
        return value

app = FastAPI()

@app.get('/ping', response_model=PingRequest)
def ping(host: str):
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}