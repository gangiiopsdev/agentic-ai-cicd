from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_safe_host(host):
    # Add your validation logic here to ensure the host is safe
    return True

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    if is_safe_host(request.host):
        args = ['ping', request.host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True to raise an exception on non-zero exit status
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}