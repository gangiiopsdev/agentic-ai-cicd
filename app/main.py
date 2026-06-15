from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await self._ping()

    async def _ping(self):
        command = ['ping', '-c', '4', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

class PingRouter:
    def __init__(self):
        pass

    def ping_router(self):
        ping_command = PingCommand(host='example.com')
        return ping_command.execute()

app = FastAPI()

@app.get("/ping")
def ping():
    ping_router = PingRouter()
    return ping_router.ping_router()