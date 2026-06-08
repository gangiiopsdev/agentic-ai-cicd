from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if ' ' in v or ';' in v or '&' in v or '|' in v:
            raise ValueError('Invalid host name')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error during ping: {e.stderr}'