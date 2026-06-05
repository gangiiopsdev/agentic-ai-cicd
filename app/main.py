from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingRouter:
    def __init__(self):
        pass

    async def ping(self, host: str):
        command = PingCommand(host)
        return await self._execute_command(command)

    async def _execute_command(self, command):
        try:
            result = await asyncio.to_thread(command.execute)
            return {'status': 'completed', 'result': result}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_router = PingRouter()

@app.get("/ping")
def ping(host: str):
    return ping_router.ping(host)