from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation with shell=False and using list for command
    subprocess.call(["ping", request.host], shell=False)
    return {"status": "completed"}