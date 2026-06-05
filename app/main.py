from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', subprocess.list2cmdline([self.host]), stdout=asyncio.subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {"status": "completed", "output": result.stdout.decode('utf-8')}