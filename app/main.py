from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Sanitize the input to avoid command injection
        sanitized_host = ''.join(c for c in request.host if c.isalnum())
        subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}