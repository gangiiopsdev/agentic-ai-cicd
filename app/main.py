from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        args = shlex.split(f'ping {self.host}')
        result = await asyncio.to_thread(subprocess.run, args, check=True, capture_output=True)
        return result.stdout.decode('utf-8')

app = FastAPI()

async def ping(host: str):
    command = PingCommand(host)
    return await command.execute()

def ping_wrapper(host: str):
    return asyncio.run(ping(host))