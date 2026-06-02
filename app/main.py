from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize user input before using it in the command
        if not request.host or ' ' in request.host:
            raise ValueError("Invalid input")
        result = subprocess.run(['ping', '-c', str(1), request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}

# Add input validation and sanitization for the host parameter