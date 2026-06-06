from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, timeout=10)
        return JSONResponse(status_code=200, content={"status": "completed", "output": output.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=400, content={"status": "error", "error": e.output.decode()})
    except subprocess.TimeoutExpired:
        return JSONResponse(status_code=408, content={"status": "timeout", "message": "Ping request timed out"})