from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the input before using it in subprocess
    if not request.host or not request.host.isalnum():
        return {"status": "error", "message": "Invalid host provided"}
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}