from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

allowed_hosts = {'example.com', 'localhost'}

@app.get("/ping")
def ping(request: PingRequest):
    if request.host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}