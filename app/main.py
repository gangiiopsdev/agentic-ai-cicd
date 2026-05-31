from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def run_safe_ping(host):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid characters in hostname")
    return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)

@app.post("/ping")
def ping(request: PingRequest):
    try:
        result = run_safe_ping(request.host)
    except ValueError as e:
        return {"status": "error", "output": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": result.stdout}