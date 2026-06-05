from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Use a whitelist of allowed hosts or validate input more strictly
        if request.host not in ['allowed_host1', 'allowed_host2']:
            return {"status": "failed", "error": "Invalid host"}
        output = subprocess.check_output(['ping', request.host], universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}