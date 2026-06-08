from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    subprocess.call(["ping", request.host.replace('.', '_')])
    return {"status": "completed"}