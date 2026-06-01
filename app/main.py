from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    # Validate the input to prevent injection attacks
    if not request.host.isalnum() or '.' not in request.host:
        return {"status": "error", "output": "Invalid host"}

    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": result.stdout}