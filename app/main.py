from fastapi import FastAPI
import subprocess
from pydantic import validator

class HostModel:
    host: str

    @validator('host')
    def validate_host(cls, v):
        # Add your validation logic here to ensure the input is safe
        if any(char in v for char in [';', '&', '|', '`']):
            raise ValueError('Invalid characters detected in host parameter')
        return v

app = FastAPI()

@app.get('/ping')
def ping(host: HostModel):
    subprocess.run(['ping', host.host], check=True)
    return {'status': 'completed'}