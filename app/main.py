from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    # Sanitize input to prevent command injection
    host = subprocess.list2cmdline([request.host])
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'error', 'error': str(e)}, status_code=500)