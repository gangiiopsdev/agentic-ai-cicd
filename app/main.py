from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() and e.isprintable())

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}