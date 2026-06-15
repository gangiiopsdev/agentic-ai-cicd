from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingResponse(BaseModel):
    status: str

def sanitize_input(input_string):
    return ''.join(char if char.isalnum() or char in ['.', '-'] for char in input_string)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return PingResponse(status=result.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status=e.stderr)