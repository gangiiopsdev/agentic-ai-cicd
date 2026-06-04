from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Secure implementation using subprocess.run
    command = ['ping', request.host]
    for arg in command:
        if not isinstance(arg, str) or not arg.isalnum():
            raise ValueError('Invalid argument provided')
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}

# Additional recommendation: Use a whitelist for allowed hostnames to further mitigate risks.