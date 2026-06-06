from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout, 'returncode': result.returncode}

@app.post("/ping")
def ping(request: PingRequest):
    result = safe_ping(request.host)
    return result