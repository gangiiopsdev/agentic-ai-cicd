from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate the input to ensure it does not contain malicious commands or arguments
    if ' ' in request.host:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', request.host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}