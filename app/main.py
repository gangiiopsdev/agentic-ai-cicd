from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate the input to ensure it's a valid hostname or IP address
    if not is_valid_host(request.host):
        return {"status": "error", "message": "Invalid host"}
    command = ["ping", request.host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host):
    # Implement validation logic here (e.g., regex to match valid hostnames/IP addresses)
    return True