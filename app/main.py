from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = {'localhost', '127.0.0.1'}

    def is_allowed_host(self, host: str) -> bool:
        return host.strip() in self.allowed_hosts

    async def ping(self, host: str):
        if not self.is_allowed_host(host):
            raise ValueError('Invalid host for ping operation')
        await asyncio.to_thread(subprocess.run, ['/bin/ping', host], check=True)

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def get_ping(host: str):
    return ping_service.ping(host)