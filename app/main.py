from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self):
        try:
            result = await self.ping_command.execute()
            return {'status': 'completed', 'result': result}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()
app.add_endpoint('/ping', PingEndpoint().ping, methods=['GET'])