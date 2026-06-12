from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    # Sanitize and validate input
    if not sanitized_host.strip():
        return {"status": "error", "output": "Invalid host provided"}

    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.output)}

@app.get("/ping")
def ping_get(host: str):
    sanitized_host = sanitize_input(host)
    return ping(PingRequest(host=sanitized_host))