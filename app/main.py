from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):    # Secure implementation
    sanitized_host = subprocess.list2cmdline([request.host])
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}