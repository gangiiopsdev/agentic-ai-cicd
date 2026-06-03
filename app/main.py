from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        valid_hosts = ['example.com', 'localhost']
        if v not in valid_hosts:
            raise ValueError('Invalid host')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):\n    cmd = ['ping', request.host]\n    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}