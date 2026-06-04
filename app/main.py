from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate input to prevent injection
    if not request.host.isalnum():
        return {"status": "error", "message": "Invalid host provided"}

    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}