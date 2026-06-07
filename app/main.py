from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
        output, _ = await result.communicate()
        return output.decode().strip()

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        status = command.execute()
        return {'status': 'completed', 'result': status}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}