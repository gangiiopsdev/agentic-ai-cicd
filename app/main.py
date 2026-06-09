from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.post('/ping')
def ping(request: PingRequest):
    safe_host = request.host.replace('.', '_').replace('-', '_')
    try:
        output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, timeout=10, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}