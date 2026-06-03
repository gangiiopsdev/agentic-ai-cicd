from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def execute_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.post('/ping')
def ping(request: PingRequest):
    return execute_ping(request.host)