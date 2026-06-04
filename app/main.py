from fastapi import FastAPI, HTTPException
import subprocess
from pydantic import BaseModel, validator
from typing import List

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

app = FastAPI()

@app.get('/ping')
def ping(host: str = Query(...)):
    try:
        result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))