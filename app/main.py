from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import uvicorn

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}