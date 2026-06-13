from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Sanitize the input to avoid command injection
    sanitized_host = subprocess.quote(request.host)
    result = subprocess.run(["ping", sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}