from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', '-c', '1', self.host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    command = PingCommand(host)\n    return {'status': 'completed', 'output': await command.execute()}