from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host')
        return v
app = FastAPI()
@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest): 
    result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}