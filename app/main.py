from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):  # Use Pydantic model to validate input
    host = request.host
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}