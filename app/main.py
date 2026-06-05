from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def run(self):
        return await self._execute()

    async def _execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            output, _ = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.run()