from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        # Define a whitelist of allowed hosts or use regex to allow specific patterns
        if not cls.is_safe_host(v):
            raise ValueError('Invalid host')
        return v

    @staticmethod
def is_safe_host(host: str) -> bool:
        # Implement your own validation logic here, e.g., using a whitelist or regex
        allowed_hosts = ['example.com', 'localhost']
        return host in allowed_hosts

@app.get('/ping')
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}