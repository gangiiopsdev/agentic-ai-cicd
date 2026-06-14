from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE)
        output, _ = await result.communicate()
        return output.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status = command.execute()
    return {'status': 'completed', 'output': status}