from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ["ping", self.host]
        result = await asyncio.create_subprocess_exec(*args)
        return {"status": "completed"}

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()