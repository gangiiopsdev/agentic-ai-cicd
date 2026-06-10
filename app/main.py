from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if len(v) > 255 or not v.strip():
            raise ValueError('Invalid hostname')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(["ping", request.host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e.stderr)
        }