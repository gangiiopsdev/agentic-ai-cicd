from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to avoid command injection
        if not request.host.isdigit():
            raise ValueError("Invalid host format")
        args = ['ping', str(request.host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}