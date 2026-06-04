from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_command = PingCommand(host)\n    result = await ping_command.execute()\n    return {"status": "completed", "output": result.stdout.decode('utf-8')}