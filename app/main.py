from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Safer implementation
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}