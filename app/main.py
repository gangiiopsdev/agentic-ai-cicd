from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Validate and sanitize host input
    if not request.host or len(request.host) > 255:\n        return {"status": "error", "output": "Invalid host input"}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:\n        return {"status": "error", "output": str(e)}