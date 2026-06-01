from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
import re

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Validate the host input to avoid shell injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
            raise ValueError('Invalid host format')
        args = ['ping', *shlex.split(request.host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}