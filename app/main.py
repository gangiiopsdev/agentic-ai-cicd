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
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}