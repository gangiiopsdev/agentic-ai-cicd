from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_valid_host(host):\n    # Regex pattern to match valid hostnames/IP addresses\n    pattern = r'^[a-zA-Z0-9.-]+$'\n    return bool(re.match(pattern, host))

@app.get("/ping")\ndef ping(request: PingRequest):\n    if not is_valid_host(request.host):\n        return {"status": "error", "message": "Invalid host"}\n    command = ["ping", request.host]\n    result = subprocess.run(command, capture_output=True, text=True, check=False)\n    return {"status": "completed", "output": result.stdout}