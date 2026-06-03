from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

global host
app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Fixed implementation
    args = ['ping', request.host]
    subprocess.call(args)
    return {"status": "completed"}