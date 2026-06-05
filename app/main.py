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
    # Use subprocess.run with shell=False and check=True to safely execute the command
    result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}