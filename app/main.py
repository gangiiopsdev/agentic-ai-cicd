from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_valid_host(host):
    return all(c.isalnum() or c in ['.', '-'] for c in host)

@app.get("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {"status": "invalid host"}, 400
    subprocess.run(['ping', request.host], check=True, capture_output=True)
    return {"status": "completed"}