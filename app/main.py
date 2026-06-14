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
    command = ['ping', '-c 4', str(host.host)]
    result = subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}