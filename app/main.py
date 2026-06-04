from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v or 'localhost' in v:
            raise ValueError('Invalid host specified')
        return v

@app.get("/ping")
def ping_endpoint(ping_request: PingRequest):
    try:
        subprocess.run(['ping', ping_request.host], check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}