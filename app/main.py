from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    try:\n        output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, timeout=5)\n        return {"status": "completed", "output": output.decode()}\n    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:\n        return {"status": "failed", "error": str(e)}