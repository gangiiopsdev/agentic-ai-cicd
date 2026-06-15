from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

def run_ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.post('/ping')
def ping(request: PingRequest):
    output = run_ping(request.host)
    return {'status': 'completed', 'output': output}