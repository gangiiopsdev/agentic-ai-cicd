from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = ['ping', '{host}']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    subprocess.call(service.ping_command.format(host=host), shell=True)
    return {"status": "completed"}