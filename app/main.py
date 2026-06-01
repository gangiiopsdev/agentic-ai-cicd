from fastapi import FastAPI
import re
from ping3 import ping

app = FastAPI()

class PingRequest(BaseModel):
    host: str
def validate_host(host):
    # Allow only alphanumeric characters and periods
    return re.match(r'^[a-zA-Z0-9.]+$', host) is not None
@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        response = ping(request.host)
        status = 'completed' if response else 'failed'
        output = f'Ping to {request.host} took {response:.2f}s' if response else ''
        return {'status': status, 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}