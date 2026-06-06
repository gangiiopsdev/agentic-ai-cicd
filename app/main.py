from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
http_basic = HTTPBasic()


class PingRequest(BaseModel):
    host: str

async def ping(host: str, credentials: HTTPBasicCredentials = Depends(http_basic)):
    if host != 'example.com':  # Example of input validation
        return {'host': host, 'error': 'Unauthorized or invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(request: PingRequest):
    return await ping(request.host)