from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    if request.host.isalnum() and len(request.host) <= 63:\n        subprocess.call(['ping', request.host], shell=False)\n        return {"status": "completed"}\n    else:\n        return {"error": "Invalid input"}