from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    host = request.host

    # Secure implementation
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}