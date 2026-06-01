from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def is_valid_host(host):
    return all(c.isalnum() or c in '.-' for c in host)
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {"status": "error", "output": "Invalid host"}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": result.stdout}