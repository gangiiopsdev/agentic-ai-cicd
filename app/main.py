from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):\n    try:\n        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)\n        return result.stdout\n    except subprocess.CalledProcessError as e:\n        return f'Error: {e.stderr}'