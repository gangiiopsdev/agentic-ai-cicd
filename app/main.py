from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'test.com'}

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            return "Host is not allowed"
        args = ['ping', *shlex.split(host)]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)