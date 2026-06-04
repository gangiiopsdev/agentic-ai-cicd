from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService(host)
    return {'status': 'completed', 'output': service.execute()}