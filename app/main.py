from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts
    if request.host not in allowed_hosts:
        return {'status': 'error', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

# Preventive Controls
# 1. Validate and sanitize user input
# 2. Use a whitelist of allowed hosts
# 3. Limit the scope of permissions for the subprocess