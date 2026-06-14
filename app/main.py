from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = await command.execute()
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}