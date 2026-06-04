from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    args = ['ping', request.host]
    subprocess.run(args)
    return {"status": "completed"}