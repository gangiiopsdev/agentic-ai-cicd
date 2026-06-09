from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate input to prevent command injection
    if not request.host.isdigit():
        return {"status": "failed", "error": "Invalid input"}
    try:
        subprocess.run(["ping", "-c 1", f'/bin/ping -c 1 {request.host}'], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}