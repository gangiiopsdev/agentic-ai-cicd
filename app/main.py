from fastapi import FastAPI
import subprocess
class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('.localdomain'):  # Example validation
            raise ValueError('Invalid hostname')
        return v

app = FastAPI()

@app.get('/ping')
def ping(host: PingRequest):
    try:
        subprocess.run(['ping', f'-c 1 {host.host}'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}