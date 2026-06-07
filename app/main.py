from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
globals = {'host': str}
app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        if request.host in globals.values():
            result = subprocess.call(['ping', request.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        else:
            return {'status': 'error', 'message': 'Invalid host'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}