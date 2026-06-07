from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not re.match(r'^[a-zA-Z0-9.-]+$', v):  # Simple regex for demonstration
            raise ValueError('Invalid hostname')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}