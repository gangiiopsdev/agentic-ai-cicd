from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingService:
    def __init__(self, allowed_hosts=[]):
        self.allowed_hosts = allowed_hosts
    def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError("Host is not allowed")
        return safe_ping(host)
app = FastAPI()
ping_service = PingService(allowed_hosts=['example.com', 'localhost'])
@app.get("/ping")
def ping(host: str):
    status = ping_service.ping(host)
    return {"status": "completed", "output": status}