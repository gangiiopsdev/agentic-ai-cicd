from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = request.host.replace(';', '').replace('&', '').replace('\', '')  # Basic sanitization
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}