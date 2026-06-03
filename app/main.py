from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with argument quoting
    subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True)
    return {"status": "completed"}