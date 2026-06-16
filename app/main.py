from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation using subprocess.run with shell=False and list arguments
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    service.ping(host)
    return {"status": "completed"}