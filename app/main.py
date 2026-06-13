from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}