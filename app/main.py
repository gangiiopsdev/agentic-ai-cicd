from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.args = ['ping', '{}']

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_service = PingService().args[1].format(host)
    subprocess.call(ping_service)
    return {"status": "completed"}