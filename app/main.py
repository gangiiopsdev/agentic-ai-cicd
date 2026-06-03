from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):   
    # Safe implementation with validation and escaping
    if not request.host.isalnum():
        return {"status": "invalid_host"}
    subprocess.call(['ping', request.host])
    return {"status": "completed"}