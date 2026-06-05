from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.host = None

    async def set_host(self, host: str):
        self.host = host

    async def execute(self):
        if self.host is not None:
            await asyncio.create_subprocess_shell(f'ping {self.host}')

app = FastAPI()
ping_command = PingCommand()

@app.get("/ping")
def ping(host: str):
    asyncio.run(ping_command.set_host(host))
    asyncio.run(ping_command.execute())
    return {'status': 'completed'}