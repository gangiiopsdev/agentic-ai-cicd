from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in v):
            raise ValueError('Invalid characters in hostname')
        return v

@app.get("/ping")
def ping(request: PingRequest):     
    args = ["ping", request.host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)    
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}