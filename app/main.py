from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

app = FastAPI()

@app.get('/')</code>