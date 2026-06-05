from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'test.com'}

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            return "Host is not allowed"
        try:
            result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

global app, ping_service
global app, ping_service
app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)