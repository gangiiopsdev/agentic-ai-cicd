from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping_host(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(request: PingRequest):
    success, output = ping_host(request.host)
    if success:
        return {"status": "completed", "result": output}
    else:
        return {"status": "failed", "error": output}