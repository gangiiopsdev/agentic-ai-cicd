from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_path = "ping"

    def ping_host(self, host: str):
        try:
            output = subprocess.run([self.ping_path, host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping_host(host)