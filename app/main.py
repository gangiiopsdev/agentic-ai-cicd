from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest(
    PydanticModel,
    base_config={'arbitrary_types_allowed': True}
):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        valid_hosts = ['example.com', 'localhost']
        if v not in valid_hosts:
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}