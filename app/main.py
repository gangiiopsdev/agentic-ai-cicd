from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', '-c 4', sanitize_host(request.host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}