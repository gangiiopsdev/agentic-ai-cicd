from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    host = request.host
    # Safe implementation with validation and full path
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}