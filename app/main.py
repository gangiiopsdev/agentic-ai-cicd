from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        return await result.communicate()

class PingRouter:
    def __init__(self):
        self.router = FastAPI()

    async def ping(self, host: str):  # type: ignore
        sanitized_host = subprocess.list2cmdline([host])
        command = PingCommand(sanitized_host)
        stdout, stderr = await command.execute()
        return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
global_router = PingRouter()
ping_router = global_router.router