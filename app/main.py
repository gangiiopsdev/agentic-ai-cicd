from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation
        subprocess.call(["ping", host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    ping_service.ping(host)
    return {"status": "completed"}