from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Safe implementation with validation
    if request.host.isnumeric() and 1 <= int(request.host) <= 254:
        args = ['ping', '-c', '1', request.host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}, 400