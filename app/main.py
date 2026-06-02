from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        cmd = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

class PingController:
    def __init__(self):
        self.ping_service = PingService()

    @app.get("/ping")
    def ping(self, host: str):
        return self.ping_service.ping(host)