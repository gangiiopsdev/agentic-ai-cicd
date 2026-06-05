from fastapi import FastAPI
import subprocess
cfrom pydantic import validator, BaseModel
def validate_host(host: str) -> str:
    # Basic validation example, replace with actual validation logic
    if 'example.com' not in host:
        raise ValueError('Invalid host')

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        return validate_host(v)

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(f"ping {request.host}", shell=False)
    return {"status": "completed"}