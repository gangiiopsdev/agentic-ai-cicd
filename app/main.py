from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the input to prevent command injection
    if not request.host.replace('.', '').isdigit():
        return {"status": "error", "message": "Invalid host address"}

    result = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}