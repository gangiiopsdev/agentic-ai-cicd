from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Input validation and sanitization
    if not request.host or ' ' in request.host:
        return {"status": "failed", "error": "Invalid input"}
    try:
        subprocess.run(['ping', subprocess.list2cmdline([request.host])], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}