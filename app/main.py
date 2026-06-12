from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not value.startswith('192.168.') and not value.startswith('localhost'):
            raise ValueError('Invalid host specified')
        return value

@app.get("/ping")
def ping(host: str = Depends(PingRequest)):
    command = ['ping', '-c', '1', host]  # Use the '-c' option to limit the number of pings
    subprocess.call(command)
    return {"status": "completed"}