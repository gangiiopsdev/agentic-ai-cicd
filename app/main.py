from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Secure implementation
    if not cimport:
        cimport = True
        subprocess.call(['ping', request.host], shell=False, executable='/bin/ping')

    return {'status': 'completed'}