from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def sanitize_host(host: str) -> str:
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', sanitize_host(request.host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}