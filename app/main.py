from fastapi import FastAPI
import subprocess
class PingService:
    def ping(host: str):
        return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    result = service.ping(host)
    if result == 0:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": "failure"}