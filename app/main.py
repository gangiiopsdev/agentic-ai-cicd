from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Validate the input to ensure it does not contain any malicious content
    if '&&' in request.host or ';' in request.host or '|':
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}