from fastapi import FastAPI
import shlex
from pydantic import BaseModel
import subprocess

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to avoid command injection
        if not request.host.isdigit():
            raise ValueError("Invalid host format")
        args = ['ping', shlex.quote(str(request.host))]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional preventive control: Use a whitelist of allowed hosts