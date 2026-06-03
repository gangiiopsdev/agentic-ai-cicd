from fastapi import FastAPI
import subprocess
from pydantic import validator

def validate_host(host: str):
    if not host or not all(c.isalnum() or c in ['-', '.', '_'] for c in host):  # Simple validation example
        raise ValueError('Invalid host')

@validator('host', pre=True)
def check_host(value):
    return validate_host(value)

class PingRequest(BaseModel):
    host: str = Field(..., description='The target host to ping')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}