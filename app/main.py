from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}