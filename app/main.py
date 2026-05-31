from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping_endpoint(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'host': request.host, 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': request.host, 'error': str(e)}