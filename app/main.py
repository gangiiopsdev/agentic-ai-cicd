from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the input
    allowed_hosts = ["google.com", "github.com"]  # Example list of allowed hosts
    if request.host not in allowed_hosts:
        return {"error": "Host is not allowed."}

    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout