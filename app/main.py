from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation with validation
    if not request.host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {"status": "completed"}