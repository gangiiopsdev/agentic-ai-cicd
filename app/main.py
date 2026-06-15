from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    args = shlex.split(f"ping {shlex.quote(request.host)}")
    subprocess.run(args, check=True)
    return {"status": "completed"}