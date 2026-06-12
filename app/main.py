from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Sanitize the input to avoid command injection
    sanitized_host = subprocess.quote(request.host)
    subprocess.run(["ping", sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed"}