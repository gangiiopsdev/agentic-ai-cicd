from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command)
        return await result.wait()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status_code = command.execute()
    return {'status': 'completed', 'exit_code': status_code}