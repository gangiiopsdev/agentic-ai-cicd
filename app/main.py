from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize user input to prevent command injection
    if not request.host.isalnum():
        return {"status": "failed", "error": "Invalid hostname"}

    try:
        output = subprocess.check_output(["ping", request.host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}