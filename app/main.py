from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Sanitize the input to prevent command injection
    sanitized_host = ''.join(c for c in request.host if c.isalnum() or c in '.-')
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}