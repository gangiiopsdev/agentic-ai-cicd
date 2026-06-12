from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

def is_valid_host(host):
    return '.' in host and not any(char.isdigit() for char in host)

@app.post("/ping")
def ping(request: PingRequest):
    try:
        if not is_valid_host(request.host):
            raise ValueError("Invalid host")
        args = ['ping', request.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}