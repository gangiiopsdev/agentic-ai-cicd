from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('-', '.'))

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}