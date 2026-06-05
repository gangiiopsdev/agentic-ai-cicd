from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):\n    # Secure implementation\n    try:\n        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n        return {"status": "completed", "output": result.stdout.decode()}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": e.stderr.decode()}