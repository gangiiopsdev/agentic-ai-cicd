from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = request.host.replace(' ', '')  # Remove spaces to prevent injection
    if not sanitized_host.isalnum():  # Ensure only alphanumeric characters are allowed
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(f'ping {sanitized_host}', shell=False)
    return {'status': 'completed'}