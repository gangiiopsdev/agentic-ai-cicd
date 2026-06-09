from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        process = await asyncio.create_subprocess_exec(*args)
        stdout, stderr = await process.communicate()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    await command.execute()
    return {"status": "completed"}