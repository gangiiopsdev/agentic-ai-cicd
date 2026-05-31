from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Vulnerable implementation
    ping_service = PingService()
    subprocess.call(ping_service.ping_command + [host])
    return {"status": "completed"}