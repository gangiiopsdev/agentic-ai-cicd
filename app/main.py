from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with full executable path
        result = subprocess.run(['/usr/bin/ping', self.host], capture_output=True, text=True)
        return result.stdout

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    service = PingService(host)
    return {'status': 'completed', 'output': service.execute()}