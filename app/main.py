from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    try:
        # Sanitize the input to prevent command injection
        safe_host = subprocess.list2cmdline([request.host])
        output = subprocess.check_output(['ping', '-c 1'] + [safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping request timed out'}