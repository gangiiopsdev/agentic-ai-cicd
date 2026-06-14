from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Safe implementation using list instead of string
    subprocess.call(['ping', request.host])
    return {"status": "completed"}