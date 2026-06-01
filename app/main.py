from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

app = FastAPI()

security = HTTPBasic()

@app.get('/ping')
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username.strip().replace(';', '').replace('&', '')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=result.returncode}