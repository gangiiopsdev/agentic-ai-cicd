from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping_route(request: PingRequest):
    try:
        output = subprocess.check_output(["ping", request.host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

# Additional preventive controls:
# 1. Validate and sanitize user input to ensure it does not contain malicious content.
# 2. Use a whitelist of allowed hosts for the ping command instead of allowing arbitrary host names.