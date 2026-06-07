from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the input
    if not request.host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}

    try:
        result = subprocess.run(['ping', request.host], check=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}