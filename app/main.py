from fastapi import FastAPI
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 64:
            raise ValueError('Invalid host name')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    args = ['ping', shlex.quote(request.host)]
    try:
        subprocess.run(args, check=True, timeout=5)  # Set a timeout to prevent command from hanging
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}