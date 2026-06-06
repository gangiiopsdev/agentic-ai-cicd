from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):\n    # Secure implementation using subprocess.run with shell=False and safely formatted arguments\n    result = subprocess.run(['ping', request.host], capture_output=True, text=True)\n    return {"status": "completed", "output": result.stdout}