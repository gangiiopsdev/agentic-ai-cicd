from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

allowed_hosts = {'127.0.0.1', 'localhost'}

@app.post("/ping")
def ping(request: PingRequest):
    if request.host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}