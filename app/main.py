from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

class PingResponse(BaseModel):
    status: str
    output: str
    error: Optional[str] = None

def safe_ping(host: str) -> PingResponse:
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return PingResponse(status='completed', output=output.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status='failed', error=str(e))

@app.post('/ping', response_model=PingResponse)
async def ping(request: PingRequest):
    return safe_ping(request.host)