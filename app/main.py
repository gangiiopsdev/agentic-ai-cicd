from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout

class PingEndpoint:
    def __init__(self):
        self.command_executor = PingCommand(host='example.com')

    async def ping(self):
        output = await self.command_executor.execute()
        return {'status': 'completed', 'output': output}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(ping_service: PingEndpoint = Depends()):
    return ping_service.ping()