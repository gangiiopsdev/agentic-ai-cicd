from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = "ping" if platform.system().lower() == "windows" else "ping -c"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    subprocess.call([service.ping_command, host])
    return {"status": "completed"}