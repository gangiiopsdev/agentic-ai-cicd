from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess with shell=False and validation
    if request.host.startswith(('http://', 'https://')):
        return {"error": "Invalid input"}
    command = ['ping', request.host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}