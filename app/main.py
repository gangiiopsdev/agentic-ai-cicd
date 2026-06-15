from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Invalid host name')
        return v

app = FastAPI()

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}