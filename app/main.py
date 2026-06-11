from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
def safe_ping(host):
    cmd = ['ping', host]
    return shlex.join(cmd)

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    try:
        output = subprocess.run(safe_ping(request.host), capture_output=True, text=True, check=True, shell=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}