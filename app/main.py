from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return result.stdout.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = safe_ping(request.host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}