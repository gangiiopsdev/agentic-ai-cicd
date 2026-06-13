from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize user input
    if not request.host.isdigit():
        return {'status': 'invalid_input'}
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {"status": "completed"}