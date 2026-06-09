from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or []

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.run(['ping', host], check=True)
            return {"status": "completed"}
        else:
            raise ValueError('Unauthorized host')

app = FastAPI()
ping_service = SafePing(allowed_hosts=['example.com'])

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)