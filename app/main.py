from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class SafePingRequest(BaseModel):
    host: str

app = FastAPI()

disallowed_hosts = ['google.com', 'example.com']

@app.get('/ping')
def ping(request: SafePingRequest):
    host = request.host
    if host in disallowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}