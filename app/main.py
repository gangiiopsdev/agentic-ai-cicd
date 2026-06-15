from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
    @validator('host', pre=True)
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in v):
            raise ValueError('Invalid hostname characters')
        return v
app = FastAPI()
@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}