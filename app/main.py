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
        output = subprocess.check_output(['ping', '-c', '4', request.host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}
    except subprocess.TimeoutExpired as e:
        return {"status": "timeout", "output": str(e)}