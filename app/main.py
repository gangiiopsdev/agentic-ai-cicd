from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e.stderr}')
@app.post("/ping")
def ping(request: PingRequest):
    safe_ping(request.host)
    return {"status": "completed"}