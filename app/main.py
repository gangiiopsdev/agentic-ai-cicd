from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def validate_host(host):
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()
class PingRequest(BaseModel):    host: str
allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts

@app.get("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}