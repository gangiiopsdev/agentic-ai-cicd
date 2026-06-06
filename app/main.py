from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if v != 'localhost':
            raise ValueError('Invalid host')

@app.post('/ping', response_model=dict)
async def ping_endpoint(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}