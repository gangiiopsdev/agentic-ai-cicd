from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get("/ping")
def ping(request: PingRequest):  # Use Pydantic model to validate input
    host = request.host
    try:
        result = subprocess.run(['ping', f'-c 1 {host}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed', 'output': result.stdout.decode()}