from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        return ''.join(c for c in v if c.isalnum() or c in ['-', '.', '_'])

app = FastAPI()

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):\n    sanitized_host = request.host\n    args = ["ping", sanitized_host]\n    subprocess.call(args)\n    return {"status": "completed"}