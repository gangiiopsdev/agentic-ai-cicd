from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Secure implementation
    args = ['ping', '-c', '1', request.host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}