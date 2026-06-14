from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

app = FastAPI()
bearer_scheme = HTTPBearer()

class Host(BaseModel):
    host: str

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}