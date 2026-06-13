from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    try:
        subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e.output)}