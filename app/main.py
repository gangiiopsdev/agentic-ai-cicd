from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host.strip()

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', '-c', '1', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = await command.execute()
    return {"status": "completed", "output": result.stdout.decode()}