from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command,
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'output': output.decode(), 'error': error.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()