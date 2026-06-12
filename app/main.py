from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class Host(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip().isdigit() and '-' not in v:
            raise ValueError('Invalid host format. Only numeric values or dash-separated values are allowed.')
        return v

@app.get("/ping")
def ping(host: Host):
    subprocess.call(['ping', '-c 4', host.host])
    return {"status": "completed"}