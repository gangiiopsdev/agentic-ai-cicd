from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Validate and sanitize input further
    if not request.host.isalnum() or '_' in request.host:
        return {'status': 'error', 'result': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': e.output.decode('utf-8')}