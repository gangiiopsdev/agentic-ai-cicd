from fastapi import FastAPI
import asyncio
from shlex import quote
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', quote(self.host), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent shell injection
    if not host.isalnum():
        raise ValueError("Invalid host input")
    command = PingCommand(host)
    return await command.execute()