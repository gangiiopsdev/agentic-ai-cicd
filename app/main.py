from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE)
        output, _ = await result.communicate()
        return output.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    output = ping_command.execute()
    return {'status': 'completed', 'output': output}