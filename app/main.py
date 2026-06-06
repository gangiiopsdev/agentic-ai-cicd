from fastapi import FastAPI
import subprocess
import shlex
import asyncio
class PingService:
    def __init__(self):
        self.allowed_hosts = {'localhost', '127.0.0.1'}

    def is_allowed_host(self, host: str) -> bool:
        return host.strip() in self.allowed_hosts

    async def ping(self, host: str):
        if not self.is_allowed_host(host):
            raise ValueError('Invalid host for ping operation')
        # Use shlex to safely quote the host argument and validate it further
        command = ['/bin/ping', shlex.quote(host)]
        await asyncio.to_thread(subprocess.run, command, check=True)

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def get_ping(host: str):
    return ping_service.ping(host)