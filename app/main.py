from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str) -> dict:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

class PingRouter:
    def __init__(self):
        self.ping_service = PingService()

    @app.get("/ping")
    def ping(self, host: str):
        return self.ping_service.ping(host)