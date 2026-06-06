from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    host = request.host
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}