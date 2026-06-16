from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def ping(host: str) -> dict:
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping_route(request: PingRequest) -> dict:
    return ping(request.host)