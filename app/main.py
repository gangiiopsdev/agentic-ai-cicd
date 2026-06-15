from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        # Using asyncio to prevent blocking the main thread
        await asyncio.create_subprocess_exec('ping', self.host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    asyncio.run(ping_command.execute())
    return {"status": "completed"}