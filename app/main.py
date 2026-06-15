from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Safe implementation with input validation
    if not request.host.strip():
        raise HTTPException(status_code=400, detail="Host parameter is required")
    subprocess.run(["ping", request.host], check=True)
    return {"status": "completed"}