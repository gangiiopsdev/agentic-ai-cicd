from fastapi import FastAPI, Request
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(request: Request, host: str):  # Use Pydantic model to validate input
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse({'status': 'completed', 'output': result.stdout.decode()})
    except (subprocess.CalledProcessError, ValueError) as e:
        return JSONResponse({'status': 'failed', 'error': str(e)}, status_code=400)