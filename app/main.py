from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Secure implementation
    subprocess.call(["ping", request.host])\n    return {"status": "completed"}