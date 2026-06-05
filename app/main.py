from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

global_host = '127.0.0.1' # Replace with appropriate default host

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, shell=False)
    return {'status': 'completed'}