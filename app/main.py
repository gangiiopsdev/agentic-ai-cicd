from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip().startswith(('127.0.0.1', '::1', 'localhost')):
            raise ValueError('Only local hosts are allowed')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', '-c', '4', request.host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}