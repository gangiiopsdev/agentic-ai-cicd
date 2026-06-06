from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not re.match(r'^[a-zA-Z0-9.-]+$', host):\n        raise HTTPException(status_code=400, detail="Invalid host")\n    ping_command = PingCommand(host)\n    result = await ping_command.execute()\n    return {"status": "completed", "output": result.stdout.decode('utf-8')}