from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    try:
        # Validate input to prevent injection attacks
        if not request.host.isalnum() or len(request.host) > 255:
            raise ValueError("Invalid hostname")
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stdout": e.stdout.decode(), "stderr": e.stderr.decode()}