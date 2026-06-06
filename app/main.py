from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
        return (await result.communicate())[0].decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output = command.execute()
    return {'status': 'completed', 'output': output}