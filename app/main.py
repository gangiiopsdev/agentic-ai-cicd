from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

# Define a model to validate the host parameter
class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    host = request.host
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}