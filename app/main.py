from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation and sanitization
    if not request.host.isalnum():
        return {"status": "error", "error": "Invalid host name"}
    try:
        result = subprocess.run(['ping', '-c', '1', subprocess.check_output(f'echo {request.host}').decode().strip()], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}