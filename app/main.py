from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping', response_model=Union[dict, dict], responses={400: {'model': dict}})
def ping(request: PingRequest):
    host = request.host
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}