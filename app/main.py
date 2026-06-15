from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get('/ping')
def ping(host: str):
    if 'localhost' not in host and '.' not in host:
        raise HTTPException(status_code=403, detail="Unauthorized access")
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error_message': e.stderr.decode()}