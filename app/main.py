from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.get("/ping")
def ping(request: PingRequest):\n    # Secure implementation\n    subprocess.call(['ping', request.host])\n    return {"status": "completed"}