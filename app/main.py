from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

class HostModel(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(host_model: HostModel):
    subprocess.run(['ping', host_model.host], check=True, shell=False)
    return {"status": "completed"}