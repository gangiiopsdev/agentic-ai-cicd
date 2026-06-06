from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.host = None

    async def set_host(self, host: str):
        self.host = subprocess.run(['ping', host], check=True)

    async def execute(self):
        if self.host is not None:
            pass  # No need to do anything here as the host is already checked in set_host

app = FastAPI()
ping_command = PingCommand()

@app.get("/ping")
def ping(host: str):
    asyncio.run(ping_command.set_host(host))
    return {'status': 'completed'}