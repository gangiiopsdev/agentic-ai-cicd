from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host):
    args = ['ping', '-c 1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
class PingRequest(BaseModel):
    host: str
@app.get('/ping')
def ping(request: PingRequest):
    return safe_ping(request.host)