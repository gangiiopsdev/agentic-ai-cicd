from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.call(args)
    return {"status": "completed"}