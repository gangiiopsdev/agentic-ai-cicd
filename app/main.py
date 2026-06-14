from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re
def sanitize_input(input_string):
    return input_string.strip().replace('\', '').replace(';', '').replace('&', '')
app = FastAPI()
class PingRequest(BaseModel):
    host: str
def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, host))
@app.get("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {"status": "error", "message": "Invalid host"}
    sanitized_host = sanitize_input(request.host)
    command = ["ping", sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}