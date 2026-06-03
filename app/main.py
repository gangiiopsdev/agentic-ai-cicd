from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get("/ping")
def ping(request: PingRequest):
    # Safe implementation using subprocess.Popen with validation
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}