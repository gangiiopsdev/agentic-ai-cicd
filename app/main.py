from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    # Fixed implementation
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}