from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()

class PingRouter:
    def __init__(self):
        self.ping_command = SafePing(host='example.com')

    @app.get('/ping')
    async def ping(self):
        stdout, stderr = await self.ping_command.execute()
        return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}

app = FastAPI()
ping_router = PingRouter()