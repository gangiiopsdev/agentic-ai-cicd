from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not re.match(r'^[a-zA-Z0-9.-]+$', v):
            raise ValueError('Invalid hostname or IP address')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=str)
def ping(request: PingRequest):
    args = ['ping', request.host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)