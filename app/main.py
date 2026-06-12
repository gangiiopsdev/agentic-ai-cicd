from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    def ping(self):
        return subprocess.call(['ping', self.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService(host)
    result = service.ping()
    if result == 0:
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}