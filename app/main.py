from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.get("/ping")
def ping(request: PingRequest):\n    # Safe implementation
    subprocess.call(["ping", request.host])\n\nreturn {"status": "completed"}