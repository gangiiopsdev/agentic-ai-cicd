from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(host_request: PingRequest):    
    subprocess.call(["ping", host_request.host])
    return {"status": "completed"}