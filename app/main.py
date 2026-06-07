from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()
class PingRequest(BaseModel):
    host: str

def run_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.post("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    result = run_ping(sanitized_host)
    return result