from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    # Secure implementation with input validation
    allowed_hosts = ['127.0.0.1', 'localhost']
    if request.host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}