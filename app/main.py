from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation using check_output to avoid shell=True and capture output
    try:
        result = subprocess.check_output(["ping", request.host], text=True, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output}