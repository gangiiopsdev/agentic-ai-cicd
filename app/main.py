from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, value):
        if not re.match(r'^[a-zA-Z0-9.-]+$', value):
            raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}