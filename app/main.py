from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):\n    args = ['ping', request.host]\n    result = subprocess.run(args, check=True, capture_output=True, text=True)\n    return {'stdout': result.stdout}