from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with shell=False and argument substitution
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}