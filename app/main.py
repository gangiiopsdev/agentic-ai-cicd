from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    if request.host.isalnum() and len(request.host) <= 63:
        # Use subprocess.run with shell=False for better security
        result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid input"}