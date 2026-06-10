from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    host = request.host
    # Secure implementation
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}