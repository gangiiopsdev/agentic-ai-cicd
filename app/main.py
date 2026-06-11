from fastapi import FastAPI
import os
import ping3
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str
def validate_host(host):
    if not host or len(host) > 255:
        raise ValueError('Invalid host')
@app.get("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        response_time = ping3.ping(request.host)
        if response_time is not None:
            return {"status": "completed", "response_time": response_time}
        else:
            return {"status": "failed"}
    except ValueError as e:
        return {'error': str(e)}