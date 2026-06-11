from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Sanitize and validate input
    if not request.host.strip():
        return {"status": "error", "output": "Invalid host provided"}

    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.output)}

@app.get("/ping")
def ping_get(host: str):
    return ping(PingRequest(host=host))