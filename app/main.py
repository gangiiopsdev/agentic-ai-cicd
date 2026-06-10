from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    try:
        ip_address = subprocess.check_output(['nslookup', request.host], stderr=subprocess.STDOUT).decode('utf-8').splitlines()[2].strip().split()[-1]
        subprocess.call(['ping', '-c', '4', ip_address])
        return JSONResponse(content={'status': 'completed'}, status_code=200)
    except Exception as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)