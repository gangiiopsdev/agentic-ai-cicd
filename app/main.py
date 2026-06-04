from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ['ping', host]

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest): 
    try:
        result = subprocess.run(safe_ping(request.host), capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}