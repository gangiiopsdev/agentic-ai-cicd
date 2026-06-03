from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Secure implementation\n    try:\n        result = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)\n        return {"status": "completed", "output": result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}