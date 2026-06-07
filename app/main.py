from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> dict:
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE)
            stdout, stderr = await output.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()