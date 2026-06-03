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

        # Use the subprocess.run method with shell=False and check=True for better security
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}