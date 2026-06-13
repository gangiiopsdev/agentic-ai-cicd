from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):  # Use Pydantic model to validate input
    host = request.host
    try:
        subprocess.call(["ping", host], shell=False)  # Avoid using shell=True
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}