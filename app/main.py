from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str) -> str:
    # Validate the input to ensure it does not contain malicious content
    if any(char in host for char in [';', '|', '&', '`']):
        raise ValueError("Invalid input")
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}
    except subprocess.TimeoutExpired:
        return {"status": "timed out"}

@app.get("/ping")
def ping(request: PingRequest):
    return safe_ping(request.host)