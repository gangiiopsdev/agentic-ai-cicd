from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
    
    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
        if v in allowed_hosts:
            return v
        raise ValueError('Invalid host')

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}