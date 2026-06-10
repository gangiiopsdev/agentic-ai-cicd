from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Safe implementation\n    result = subprocess.run(['ping', request.host], capture_output=True, text=True)\n    return {"status": "completed", "output": result.stdout}