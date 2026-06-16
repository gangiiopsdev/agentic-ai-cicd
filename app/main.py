from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']  # Add other allowed hosts here
    if request.host in allowed_hosts:
        subprocess.call(['ping', request.host], shell=False)
        return {"status": "completed"}
    else:
        return {'error': 'Unauthorized host'}, 403