from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    sanitized_host = request.host.replace(' ', '').replace('\t', '').replace('\n', '')
    if not any(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in sanitized_host):
        return {'error': 'Invalid input'}
    args = ['ping', '--', sanitized_host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}