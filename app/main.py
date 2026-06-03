from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    if not request.host.strip():
        raise ValueError('Host parameter is empty or invalid')
    subprocess.run(['ping', *request.host.split()], check=True)
    return {'status': 'completed'}