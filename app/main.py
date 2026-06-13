from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, value):
        if not re.match(r'^[a-zA-Z0-9.-]+$', value):
            raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, capture_output=True)
    return {"status": "completed"}