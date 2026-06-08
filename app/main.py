from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):\n    # Secure implementation
    subprocess.run(['ping', request.host], check=True, shell=False)
    return {'status': 'completed'}