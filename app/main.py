from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Safe implementation using subprocess.run with input validation
    if request.host.strip().isdigit():
        args = ['ping', request.host]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        raise ValueError('Invalid host')