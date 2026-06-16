from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', *shlex.split(shlex.quote(self.host)), stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {'status': 'completed', 'result': result}