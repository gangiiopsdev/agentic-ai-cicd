from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

global_host = '127.0.0.1' # Replace with appropriate default host

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(["ping", request.host])
    return {"status": "completed"}