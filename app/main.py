from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand(None)

    async def ping(self, host: str):
        self.ping_command.host = host
        output, error = await self.ping_command.execute()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.ping(host)