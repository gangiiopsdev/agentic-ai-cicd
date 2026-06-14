from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def run_ping(request: PingRequest) -> dict:
    try:
        safe_host = shlex.quote(request.host)
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest) -> dict:
    return run_ping(request)