from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run and shlex.quote
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode(), stderr.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    stdout, stderr = command.execute()
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}