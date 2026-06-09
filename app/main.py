from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Safe implementation using subprocess.run with list of arguments and validate input
        if not request.host.isalnum():
            raise ValueError('Invalid host name')
        subprocess.run(['ping', request.host], check=True, capture_output=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}