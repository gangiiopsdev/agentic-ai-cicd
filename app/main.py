from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host):
    args = ['ping', '-c', '4', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.post("/ping")
def ping(request: PingRequest):
    try:
        output = safe_ping(request.host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}