from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status, result = await command.execute()
    return {"status": "completed", "result": result}