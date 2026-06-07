from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def validate_host(host):
    # Basic validation to ensure the host does not contain unexpected characters
    if any(char in host for char in [';', '&', '|', '&&', '||', '`']):
        raise ValueError('Invalid host input')
app = FastAPI()
class PingRequest(BaseModel):
    host: str
@app.get("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}