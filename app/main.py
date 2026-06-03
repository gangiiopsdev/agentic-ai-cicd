from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get('/ping')
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts to prevent command injection
        allowed_hosts = ['google.com', 'example.com']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}

        # Use a safer method to execute the ping command with absolute path
        output = subprocess.check_output(['/bin/ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}