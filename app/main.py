from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get('/ping')
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with shell=False and properly quoted arguments
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}