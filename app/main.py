from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_command = PingCommand(host)\n    process = await ping_command.execute()\n    # Handle the process result if needed\n    return {"status": "completed"}