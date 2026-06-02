from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    host = request.host.strip()
    if not host or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])
    return {'status': 'completed'}