from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

class PingRouter:
    def __init__(self):
        self.router = FastAPI()

    async def ping(self, host: str):
        command = PingCommand(host)
        result = await self.run_command(command.execute())
        return {'status': 'completed', 'result': result}

    @staticmethod
    async def run_command(command_func):
        import asyncio
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, command_func)
        return result

global_router = PingRouter()
app.include_router(global_router.router)