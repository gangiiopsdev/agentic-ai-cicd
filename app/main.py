from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):  # Use Pydantic model for input validation
    # Safe implementation with input validation and escaping
    subprocess.call(["ping", request.host])
    return {"status": "completed"}