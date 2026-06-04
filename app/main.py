from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not value.strip():
            raise ValueError('Host cannot be empty or whitespace')
        return value

@app.get("/ping")
def ping(request: PingRequest):

    # Secure implementation
    args = ['ping', request.host]
    subprocess.call(args)

    return {"status": "completed"}