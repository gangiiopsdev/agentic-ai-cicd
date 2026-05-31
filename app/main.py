from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": result.stdout}