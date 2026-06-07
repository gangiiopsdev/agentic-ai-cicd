from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> str:
        return await self._ping()

    async def _ping(self) -> str:
        command = ['ping', self.host]
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host.replace(' ', ''))  # Sanitize input to prevent command injection
    result = ping_command.execute()
    return {'status': 'completed', 'output': await result}