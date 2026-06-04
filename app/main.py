from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        args = ['ping', self.host]
        await asyncio.create_subprocess_exec(*args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    await command.run()
    return {"status": "completed"}