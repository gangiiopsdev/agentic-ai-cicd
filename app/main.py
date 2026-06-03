from fastapi import FastAPI
import subprocess

class PingService:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or ['google.com', 'example.com']

    async def ping(self, host: str) -> dict:
        if not await self.validate_host(host):
            raise ValueError("Invalid host")
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "result": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

    async def validate_host(self, host: str) -> bool:
        return host in self.allowed_hosts

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)