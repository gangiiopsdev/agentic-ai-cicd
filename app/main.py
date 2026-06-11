from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    result = subprocess.run(["ping", "-c", "1", request.host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}