from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
gl
app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    command = ["ping", request.host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}