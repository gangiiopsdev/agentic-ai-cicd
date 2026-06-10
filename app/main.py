from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    request = PingRequest(host)
    subprocess.call(['ping', request.host])
    return {"status": "completed"}