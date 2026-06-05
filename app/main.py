from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    host = request.host
    if host in ['localhost', '127.0.0.1']:  # Add more checks as necessary
        subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}