from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Secure implementation
    try:
        subprocess.call(['ping', request.host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500