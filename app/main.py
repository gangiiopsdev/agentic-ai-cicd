from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Fixed implementation
    if not request.host.startswith(('192.168.', '10.', '172.')):
        raise ValueError('Invalid host')
    subprocess.call(['ping', request.host], shell=False)
    return {'status': 'completed'}