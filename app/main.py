from fastapi import FastAPI
import subprocess

class PingRequest:
    def __init__(self, host: str):
        self.host = host

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    sanitized_host = ''.join(c for c in request.host if c.isalnum() or c in ['-', '.', '_'])
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}