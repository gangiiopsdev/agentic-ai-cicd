from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand('127.0.0.1')  # Default host

    async def ping(self, host=None):
        if host is not None:
            self.ping_command.host = host
        return await self.ping_command.execute()

class PingRouter:
    def __init__(self):
        self.ping_endpoint = PingEndpoint()

    @app.get("/ping")
    async def ping(self, host: str=None):
        status, output = await self.ping_endpoint.ping(host)
        return {'status': 'completed', 'output': output.decode()}