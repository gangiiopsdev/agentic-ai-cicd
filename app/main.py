from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    # Simple validation to allow only alphanumeric characters and some common separators
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid host")

@app.get('/ping')
def ping(request: PingRequest):
    validate_host(request.host)
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}