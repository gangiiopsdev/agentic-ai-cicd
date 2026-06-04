from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

def safe_ping(host: str):
    if not host or len(host) > 255:
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    output = safe_ping(request.host)
    return {"status": "completed", "output": output}