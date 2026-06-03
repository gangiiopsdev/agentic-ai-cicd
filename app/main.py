from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.isdigit():  # Example validation, use appropriate logic for your application
            raise ValueError('Invalid host format')

@app.get("/ping")
def ping(request: PingRequest):
    try:
        subprocess.run(['ping', f'--{request.host}'], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}