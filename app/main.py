from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}