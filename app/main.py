from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ["ping", self.host]
        process = await asyncio.create_subprocess_exec(*args, check=True, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        return {"status": "completed", "stdout": process.stdout.decode(), "stderr": process.stderr.decode()}
global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()