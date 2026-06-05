from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').replace('-', '').isalnum():
        raise ValueError('Invalid hostname')
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {"status": "completed", "output": result.stdout.decode('utf-8')}